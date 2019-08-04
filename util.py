import os
import config
import numpy as np  # type: ignore
from typing import Union, Type


def make_directory(
    Config: Union[Type[config.ENConfig], Type[config.SOMConfig], Type[config.HNConfig]]
) -> str:
    dir_name = "./results/%s/%s/" % (Config.city_file.replace(".csv", ""), Config.name)
    directory = os.path.dirname(dir_name)
    os.makedirs(directory, exist_ok=True)
    return dir_name


def dist(p1: np.array, p2: np.array) -> np.array:
    return np.linalg.norm(p1 - p2)
