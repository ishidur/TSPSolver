import sys
sys.path.append('..') # this required for import script in parent dirctory
import hopfield_network as hn
import numpy as np


def test_sigmoid():
    a = np.array([0, 1000, -1000])
    a_0 = 0
    a_1 = 1000
    a_2 = -1000
    b = hn.sigmoid(a)
    b_0 = hn.sigmoid(a_0)
    b_1 = hn.sigmoid(a_1)
    b_2 = hn.sigmoid(a_2)
    assert b.all() == np.array([b_0, b_1, b_2]).all()
