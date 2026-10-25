#!/usr/bin/env bash
set -euo pipefail
# Fail closed. Intended for macOS external-drive layout; do not create mountpoints.
if [[ "$(uname -s)" != "Darwin" ]]; then
  echo 'This check is for the macOS external-drive workflow only.' >&2
  exit 2
fi
for p in /Volumes/T7Projects /Volumes/T7Tmp; do
  if [[ ! -d "$p" || -L "$p" ]]; then
    echo "REQUIRED MOUNT MISSING or symbolic link: $p" >&2
    exit 3
  fi
  if ! /sbin/mount | grep -F " on $p (" >/dev/null; then
    echo "NOT A VERIFIED MOUNT: $p — refusing heavy workload" >&2
    exit 4
  fi
  echo "Verified mounted volume: $p"
done
echo 'External mountpoints present; separately verify source volume identities before sensitive work.'
