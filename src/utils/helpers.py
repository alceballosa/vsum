import configparser
from pathlib import Path


def parse_dict(d: dict) -> dict:
    """
    Parses the values of a dictionary into their respective datatypes, which can
    include: string, int, float, boolean. The values can also be nested dicts.
    """
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = parse_dict(v)
        elif isinstance(v, str):
            if v.lower() == "true":
                d[k] = True
            elif v.lower() == "false":
                d[k] = False
            else:
                try:
                    d[k] = int(v)
                except ValueError:
                    try:
                        d[k] = float(v)
                    except ValueError:
                        pass
    return d


def read_config_file(filepath: Path) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(filepath)
    return config
