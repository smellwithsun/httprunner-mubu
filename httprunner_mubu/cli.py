import argparse
import sys

#命令行调用
from httprunner_mubu.runner import run_yaml


def main():
    """ API test: parse command line options and run commands.
    """

    parser = argparse.ArgumentParser(description="httprunner_mubu")
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version")
    parser.add_argument(
        'yaml_paths',
        help="yaml file path")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        # no argument passed
        parser.print_help()
        return 0
    print("testpath----------",args.yaml_paths)
    success = run_yaml(args.yaml_paths)
    return success


if __name__ == '__main__':
    main()


#运行方式：httprunner-mubu neo$ python -m httprunner_mubu.cli -h
