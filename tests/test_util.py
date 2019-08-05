import sys

sys.path.append("..")  # this required for import script in parent dirctory
import util
import numpy as np  # type: ignore

def test_dist():
    a = np.array([10, 0])
    b = np.array([0, 0])
    assert util.dist(a, b) == 10
    a = np.array([0, 10])
    b = np.array([0, 0])
    assert util.dist(a, b) == 10
    a = np.array([-10, 0])
    b = np.array([0, 0])
    assert util.dist(a, b) == 10
    a = np.array([0, -10])
    b = np.array([0, 0])
    assert util.dist(a, b) == 10
    a = np.array([0, 10])
    b = np.array([10, 0])
    assert util.dist(a, b) == np.sqrt(2) * 10
    a = np.array([10, 2])
    b = np.array([5, -10])
    assert util.dist(a, b) == 13
