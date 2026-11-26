#!/usr/bin/env python3
"""푸시된 main의 교수용 HTML을 다시 내려받아 로컬 SHA256과 비교한다."""

import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent.parent


def main():
    local = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    remote = subprocess.check_output(['git', 'ls-remote', 'origin', 'refs/heads/main'], cwd=ROOT, text=True).split()[0]
    assert local == remote, 'local and remote main differ'
    course = json.loads((ROOT / 'course.json').read_text())
    files = ['course.json', 'assets/site.js', 'index.html'] + [f"{c['slug']}_{c['version']}.html" for c in course['chapters']]
    for file in files:
        url = f'https://raw.githubusercontent.com/Yuul-Jung/system_verilog_uvm_tb_teach/{remote}/{file}'
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
        expected = hashlib.sha256((ROOT / file).read_bytes()).hexdigest()
        actual = hashlib.sha256(data).hexdigest()
        assert expected == actual, f'remote bytes differ: {file}'
        print(f'PASS remote {file} SHA256={actual}')
    print(f'PASS local=remote={remote}')


if __name__ == '__main__':
    main()
