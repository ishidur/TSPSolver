import sys

sys.path.append("..")  # this required for import script in parent dirctory
import hopfield_network as hn
import numpy as np  # type: ignore

#############################################################################
# Here are unit tests
#############################################################################
def test_sigmoid():
    a = np.array([0, 1000, -1000])
    a_0 = 0
    a_1 = 1000
    a_2 = -1000
    b = hn.sigmoid(a)
    b_0 = hn.sigmoid(a_0)
    b_1 = hn.sigmoid(a_1)
    b_2 = hn.sigmoid(a_2)
    assert (b == np.array([b_0, b_1, b_2])).all()


def test_kronecker_delta():
    assert hn.kronecker_delta(0, 0) == 1.0
    assert hn.kronecker_delta(0, 1) == 0.0
    assert hn.kronecker_delta(1, 0) == 0.0
    assert hn.kronecker_delta(1, 1) == 1.0


def test_calc_weight_matrix():
    # Set same contidions to TSPHopfieldEigen, C++ Project
    hn.param_a = 1.0
    hn.param_b = 1.0
    hn.param_c = 2.0
    hn.param_d = 1.0
    # fmt: off
    cities = [
      [0.5, 0.9],
      [0.2, 0.8],
      [0.15, 0.25],
      [0.4, 0.5],
      [0.25, 0.1],
      [0.65, 0.3],
      [0.6, 0.3],
      [0.9, 0.35],
      [0.9, 0.7],
      [0.7, 0.5],
    ]
    # fmt: on
    city_arr = np.array(cities)
    res = hn.calc_weight_matrix(city_arr)
    expected_array_size = len(cities) ** 2
    assert res.shape == (expected_array_size, expected_array_size)
    expected_weight = np.loadtxt("./expected_weights.csv", delimiter=",")
    assert res.shape == expected_weight.shape
    assert (np.round(res, decimals=5) == np.round(expected_weight, decimals=5)).all()
    # for i in range(expected_array_size):
    #     for j in range(expected_array_size):
    #         assert np.round(res[i][j], decimals=5) == np.round(
    #             expected_weight[i][j], decimals=5
    #         )


def test_calc_bias():
    # Set same contidions to TSPHopfieldEigen, C++ Project
    hn.param_c = 2.0
    # fmt: off
    cities = [
      [0.5, 0.9],
      [0.2, 0.8],
      [0.15, 0.25],
      [0.4, 0.5],
      [0.25, 0.1],
      [0.65, 0.3],
      [0.6, 0.3],
      [0.9, 0.35],
      [0.9, 0.7],
      [0.7, 0.5],
    ]
    # fmt: on
    city_arr = np.array(cities)
    res = hn.calc_bias(city_arr)
    expected_array_size = len(cities) ** 2
    assert res.shape == (expected_array_size,)
    expected_biases = np.loadtxt("./expected_biases.csv", delimiter=",")
    assert res.shape == expected_biases.shape
    assert (np.round(res, decimals=5) == np.round(expected_biases, decimals=5)).all()

