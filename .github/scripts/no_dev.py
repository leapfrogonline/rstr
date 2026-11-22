import glob
import re
import sys

RELEASE = re.compile(r'^\d+\.\d+\.\d+$')


def main() -> int:
    distributions = glob.glob('dist/*.whl') + glob.glob('dist/*.tar.gz')
    if not distributions:
        print('::error::no distributions found in dist/')
        return 1

    status = 0
    for path in sorted(distributions):
        filename = path.rsplit('/', 1)[-1]
        stem = filename.removesuffix('.whl').removesuffix('.tar.gz')
        parts = stem.split('-')
        version = parts[1] if len(parts) > 1 else ''
        if not RELEASE.fullmatch(version):
            print(f'::error::refusing to publish {filename}: version {version!r} is not a release')
            status = 1
            continue

        print(f'publishing {filename}')

    return status


if __name__ == '__main__':
    sys.exit(main())
