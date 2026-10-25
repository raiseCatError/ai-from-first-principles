import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from tracker.__main__ import load_course, load_progress, validate, report_markdown, save

class CurriculumTests(unittest.TestCase):
    def test_course_complete_and_valid(self):
        validate(load_course(), load_progress())
    def test_every_week_page_exists(self):
        base = Path(__file__).resolve().parents[1]
        for item in load_course():
            path = base / 'weeks' / f'{item["week"]:02d}.md'
            self.assertTrue(path.is_file(), str(path))
            self.assertIn(item['title'], path.read_text())
    def test_every_resource_key_exists(self):
        base=Path(__file__).resolve().parents[1]
        links=json.loads((base/'resources/links.json').read_text())
        for wk in load_course():
            for ref in wk['resources']:
                self.assertIn(ref,links)
                self.assertTrue(links[ref].startswith('https://'))
    def test_report_has_48_rows(self):
        report=report_markdown(load_course(), load_progress())
        self.assertEqual(sum(x.startswith('| [') for x in report.splitlines()),48)
    def test_atomic_save(self):
        with TemporaryDirectory() as folder:
            path=Path(folder)/'progress.json'
            save({'test':True},path)
            self.assertEqual(json.loads(path.read_text()),{'test':True})
    def test_done_without_evidence_is_rejected(self):
        p=load_progress();p['weeks']['01']['state']='done'
        with self.assertRaisesRegex(ValueError,'no evidence'):
            validate(load_course(),p)

if __name__ == '__main__':
    unittest.main()

class TrackerMutationTests(unittest.TestCase):
    def test_start_done_and_reset_using_isolated_file(self):
        import contextlib
        import io
        from unittest.mock import patch
        import tracker.__main__ as tr
        with TemporaryDirectory() as tmp:
            fake_progress=Path(tmp)/'progress.json'
            tr.save(tr.load_progress(), fake_progress)
            with patch.object(tr,'PROGRESS',fake_progress), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(tr.cli(['start','1']),0)
                self.assertEqual(tr.load_progress()['weeks']['01']['state'],'in-progress')
                self.assertEqual(tr.cli(['done','1','--evidence','experiments/first-run.md']),0)
                self.assertEqual(tr.load_progress()['weeks']['01']['state'],'done')
                self.assertEqual(tr.cli(['reset','1']),0)
                self.assertEqual(tr.load_progress()['weeks']['01']['state'],'not-started')
