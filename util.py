import os
import config
from typing import Union


def make_directory(
    Config: Union[config.ENConfig, config.SOMConfig, config.HNConfig]
) -> str:
    dir_name = "./results/%s/%s/" % (Config.city_file.replace(".csv", ""), Config.name)
    directory = os.path.dirname(dir_name)
    os.makedirs(directory, exist_ok=True)
    return dir_name
