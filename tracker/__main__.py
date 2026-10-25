"""Usage: python3 -m tracker [status|next|show|start|done|block|reset|report|validate]."""
from __future__ import annotations
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / 'curriculum' / 'weeks.json'
PROGRESS = ROOT / 'progress.json'
STATES = ('not-started', 'in-progress', 'blocked', 'done')


def load_course() -> list[dict]:
    return json.loads(COURSE.read_text(encoding='utf-8'))


def load_progress() -> dict:
    return json.loads(PROGRESS.read_text(encoding='utf-8'))


def validate(course: list[dict], progress: dict) -> None:
    if [w['week'] for w in course] != list(range(1, 49)):
        raise ValueError('Course must contain weeks 1..48 exactly once in order.')
    if set(progress['weeks']) != {f'{i:02d}' for i in range(1, 49)}:
        raise ValueError('Progress must contain exactly week IDs 01..48.')
    for w in course:
        for key in ('phase', 'title', 'study', 'math', 'build', 'verify', 'resources'):
            if not w.get(key):
                raise ValueError(f'Week {w["week"]}: missing {key}')
        entry = progress['weeks'][f'{w["week"]:02d}']
        if entry['state'] not in STATES:
            raise ValueError(f'Invalid state for week {w["week"]}')
        if not isinstance(entry.get('evidence'), list):
            raise ValueError(f'Evidence must be a list for week {w["week"]}')
        if entry['state'] == 'done' and not entry['evidence']:
            raise ValueError(f'Week {w["week"]} is done but has no evidence')


def save(data: dict, path: Path | None = None) -> None:
    if path is None:
        path = PROGRESS
    text = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as f:
        f.write(text)
        name = f.name
    os.replace(name, path)


def get_week(course: list[dict], week: int) -> dict:
    if week < 1 or week > len(course):
        raise ValueError('Week must be between 1 and 48.')
    return course[week - 1]


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def report_markdown(course: list[dict], progress: dict) -> str:
    counts = {state: sum(entry['state'] == state for entry in progress['weeks'].values()) for state in STATES}
    lines = ['# Learning progress', '', f'**Done:** {counts["done"]}/48 · **In progress:** {counts["in-progress"]} · **Blocked:** {counts["blocked"]}',
             '', '| Week | Topic | State | Evidence |', '|---:|---|---|---|']
    for w in course:
        k = f'{w["week"]:02d}'
        p = progress['weeks'][k]
        ev = ', '.join(p['evidence']) if p['evidence'] else '—'
        ev = ev.replace('|', '\\|').replace('\n', ' ')
        lines.append(f'| [{k}](weeks/{k}.md) | {w["title"]} | {p["state"]} | {ev} |')
    lines += ['', 'Generated using `python3 -m tracker report`. Source of truth: `progress.json`.', '']
    return '\n'.join(lines)


def cli(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description='Track implementation-first AI study progress')
    sub = p.add_subparsers(dest='command', required=True)
    for name in ('status','next','report','validate'):
        sub.add_parser(name)
    for name in ('show','start','reset'):
        x = sub.add_parser(name)
        x.add_argument('week', type=int)
    x = sub.add_parser('done')
    x.add_argument('week', type=int)
    x.add_argument('--evidence', required=True, help='File path, commit SHA or experiment ID')
    x = sub.add_parser('block')
    x.add_argument('week', type=int)
    x.add_argument('--reason', required=True)
    args = p.parse_args(argv)
    course, progress = load_course(), load_progress()
    validate(course, progress)
    if args.command == 'validate':
        print('Valid: 48 complete weekly plans and consistent progress data.')
        return 0
    if args.command == 'status':
        done = sum(x['state'] == 'done' for x in progress['weeks'].values())
        print(f'Completed: {done}/48 weeks ({done/48:.0%})')
        print('  Wk  State        Topic')
        for w in course:
            k=f'{w["week"]:02d}'
            print(f'  {k}  {progress["weeks"][k]["state"]:<12} {w["title"]}')
        return 0
    if args.command == 'next':
        next_week = next((w for w in course if progress['weeks'][f'{w["week"]:02d}']['state'] != 'done'), None)
        if next_week:
            print(f'Next: week {next_week["week"]:02d} — {next_week["title"]}\nRead weeks/{next_week["week"]:02d}.md')
        else:
            print('All 48 weeks completed. Time to propose a new research question!')
        return 0
    if args.command == 'report':
        target=ROOT / 'PROGRESS.md'
        target.write_text(report_markdown(course, progress), encoding='utf-8')
        print(f'Wrote {target.relative_to(ROOT)}')
        return 0
    week = get_week(course,args.week)
    key = f'{args.week:02d}'
    entry=progress['weeks'][key]
    if args.command == 'show':
        print(f'{key}: {week["title"]}\nPhase: {week["phase"]}\nStatus: {entry["state"]}\nStudy: {week["study"]}\nMath: {week["math"]}\nBuild: {week["build"]}\nCheck: {week["verify"]}\nFile: weeks/{key}.md')
        return 0
    if args.command == 'start':
        if entry['state'] == 'done':
            print('Already completed. Reset explicitly if you really intend to restart.')
            return 1
        entry['state']='in-progress'; entry['started_at']=entry.get('started_at') or now();entry['blocked_reason']=None
    elif args.command == 'done':
        evidence=args.evidence.strip()
        if not evidence:
            p.error('--evidence must not be empty')
        if evidence not in entry['evidence']:
            entry['evidence'].append(evidence)
        entry['state']='done';entry['completed_at']=now();entry['blocked_reason']=None
    elif args.command == 'block':
        reason=args.reason.strip()
        if not reason: p.error('--reason must not be empty')
        entry['state']='blocked';entry['blocked_reason']=reason
    elif args.command == 'reset':
        entry.update({'state':'not-started','evidence':[],'started_at':None,'completed_at':None,'blocked_reason':None})
    save(progress)
    print(f'Week {key}: {entry["state"]}')
    return 0

if __name__ == '__main__':
    raise SystemExit(cli())
