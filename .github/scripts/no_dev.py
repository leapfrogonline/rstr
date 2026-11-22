import glob
import sys

from packaging.utils import parse_wheel_filename


def main() -> int:
    wheels = glob.glob('dist/*.whl')
    if not wheels:
        print('::error::no wheel found in dist/')
        return 1

    wheel = wheels[0].rsplit('/', 1)[-1]
    version = parse_wheel_filename(wheel)[1]
    if version.dev is not None:
        print(f'::error::refusing to publish development version {version}')
        return 1

    print(f'publishing {version}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
