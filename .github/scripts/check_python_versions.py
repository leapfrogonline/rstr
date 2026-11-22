import json
import re
import sys
import tomllib
import urllib.request
from pathlib import Path

RELEASES_URL = 'https://endoflife.date/api/python.json'


def version_key(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split('.'))


def main() -> int:
    config = tomllib.loads(Path('pyproject.toml').read_text())
    envs = config['tool']['tox']['env_list']
    tested = {f'{env[2]}.{env[3:]}' for env in envs if re.fullmatch(r'py3\d+', env)}
    if not tested:
        print('no py3* environments found in tool.tox.env_list')
        return 1

    with urllib.request.urlopen(RELEASES_URL) as response:
        releases = json.load(response)
    released = {entry['cycle'] for entry in releases if re.fullmatch(r'3\.\d+', entry['cycle'])}

    newest_tested = max(tested, key=version_key)
    newer = {v for v in released if version_key(v) > version_key(newest_tested)}
    untested = sorted(newer - tested, key=version_key)

    print(f'tested: {sorted(tested, key=version_key)}')
    print(f'released: {sorted(released, key=version_key)}')
    if untested:
        print(f'::error::untested Python releases: {untested}')
        print(f'Add matching py3N entries to tool.tox.env_list (newest tested: {newest_tested})')
        return 1

    print(f'all released versions up to {newest_tested} are tested')
    return 0


if __name__ == '__main__':
    sys.exit(main())
