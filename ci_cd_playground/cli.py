import argparse
import os.path
import yaml


def build_parser():
    """
    Build parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', dest='config', action='store', type=str,
        help='path to custom config',
        default=os.path.join(os.path.dirname(__file__), "config.yaml")
    )
    return parser


def load_config(file_name):
    """
       Load config
       :param file_name
    """
    with open(file_name,"r") as conf_file:
        return yaml.safe_load(conf_file.read())


def main():
    """
       Do some magic
    """
    parser = build_parser()
    params, other_params = parser.parse_known_args()
    conf = load_config(params.config)
    print(conf)


if __name__ == "__main__":
    main()
