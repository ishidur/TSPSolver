from config import HNConfig as Config
import numpy as np  # type: ignore
from matplotlib import pyplot as plt  # type: ignore
from matplotlib import cm  # type: ignore
from matplotlib import colors  # type: ignore
import pandas as pd  # type: ignore
import util

window_size = 5
dpi = 100
iter_lim = 10000
record_moment = np.arange(0, iter_lim, 10)
record = False
delta_t = 0.001
noise = 0.01
u_0 = 0.02
param_a = 500.0
param_b = 500.0
param_c = 200.0
param_d = 500.0


@np.vectorize
def sigmoid(input: float) -> float:
    sigmoid_range = 34.538776394910684
    if input <= -sigmoid_range:
        return 1e-15
    if input >= sigmoid_range:
        return 1.0 - 1e-15
    return 1.0 / (1.0 + np.exp(-input / u_0))


def kronecker_delta(i: float, j: float) -> float:
    if i == j:
        return 1.0
    return 0.0


def calc_weight_matrix(city_array: np.array) -> np.array:
    city_num = city_array.shape[0]
    n = city_num ** 2
    tmp = np.zeros((n, n))
    for s0 in range(n):
        x = int(s0 / city_num)
        i = s0 % city_num
        for s1 in range(n):
            y = int(s1 / city_num)
            j = s1 % city_num
            dxy = util.dist(city_array[x, :], city_array[y, :])
            tmp[s0, s1] = (
                -param_a * kronecker_delta(x, y) * (1.0 - kronecker_delta(i, j))
                - param_b * kronecker_delta(i, j) * (1.0 - kronecker_delta(x, y))
                - param_c
                - param_d
                * dxy
                * (
                    kronecker_delta(j, (i - 1) % city_num)
                    + kronecker_delta(j, (i + 1) % city_num)
                )
            )
    df = pd.DataFrame(tmp)
    df.to_csv("weigths.csv")
    return tmp


def calc_bias(city_array: np.array) -> np.matrix:
    city_num = city_array.shape[0]
    n = city_num ** 2
    tmp = param_c * n * np.ones(n)
    return tmp


def update_inner_vals(
    nodes_array: np.matrix,
    inner_vals: np.matrix,
    weight_matrix: np.matrix,
    biases: np.matrix,
) -> np.matrix:
    tau = 1.0
    asdf = np.matmul(weight_matrix, nodes_array)
    delta = (-inner_vals / tau + asdf + biases) * delta_t
    return inner_vals + delta


def hp_begin(
    inner_vals_array: np.matrix,
    nodes_array: np.matrix,
    weights_matrix: np.matrix,
    biases_array: np.matrix,
):
    if record:
        dir_name = util.make_directory(Config)
        for i in range(iter_lim):
            if i in record_moment:
                filename = "iteration-" + str(i) + ".png"
                file_path = dir_name + filename
                plt.savefig(file_path)
            inner_vals_array = update_inner_vals(
                nodes_array, inner_vals_array, weights_matrix, biases_array
            )
            nodes_array = sigmoid(inner_vals_array)
            plt.title("iteration=" + str(i + 1))
            mat_visual.set_data(np.reshape(nodes_array, (city_num, city_num)))
            plt.pause(0.0001)
    else:
        i = 1
        # while plt.get_fignums():
        # inner_vals_array = update_inner_vals(nodes_array, inner_vals_array, weights_matrix, biases_array)
        # nodes_array = sigmoid(inner_vals_array)
        # plt.title("iteration=" + str(i))
        # mat_visual.set_data(np.reshape(nodes_array, (city_num, city_num)))
        # i += 1
        # plt.pause(.01)
        while plt.get_fignums():
            # print(nodes_array.shape, inner_vals_array.shape, weights_matrix.shape, biases_array.shape)
            inner_vals_array = update_inner_vals(
                nodes_array, inner_vals_array, weights_matrix, biases_array
            )
            nodes_array = sigmoid(inner_vals_array)
            plt.title("iteration=" + str(i))
            mat_visual.set_data(np.reshape(nodes_array, (city_num, city_num)))
            i += 1
            plt.pause(0.0001)


if __name__ == "__main__":
    if Config.read_file:
        np_cities = np.genfromtxt(Config.file_path + Config.city_file, delimiter=",")
        city_num = np_cities.shape[0]
        # width_x = (np.max(np_cities[:, 0]) - np.min(np_cities[:, 0]))
        # width_y = (np.max(np_cities[:, 1]) - np.min(np_cities[:, 1]))
        # width = np.amax([width_x, width_y])
        # np_cities[:, 0] -= np.min(np_cities[:, 0])
        # np_cities[:, 0] /= width
        # np_cities[:, 1] -= np.min(np_cities[:, 1])
        # np_cities[:, 1] /= width
        # center_x = np.average(np_cities[:, 0])
        # center_y = np.average(np_cities[:, 1])
        figsize = (window_size, window_size)
    else:
        city_num = Config.city_num
        # “continuous uniform” distribution random
        np_cities = np.random.random((city_num, 2))
        center_x = 0.5
        center_y = 0.5
        figsize = (window_size, window_size)
    inner_vals = np.matrix((np.random.random((city_num ** 2)) - 0.5) * noise).T
    nodes = np.matrix(sigmoid(inner_vals))
    weights = np.matrix(calc_weight_matrix(np_cities))
    biases = np.matrix(calc_bias(np_cities)).T
    fig = plt.figure(figsize=figsize, dpi=dpi)
    mat_visual = plt.matshow(
        np.reshape(nodes, (city_num, city_num)),
        fignum=0,
        cmap=cm.Greys,
        norm=colors.Normalize(vmin=0.0, vmax=1.0),
    )
    fig.colorbar(mat_visual)
    plt.title("iteration=" + str(0))
    plt.pause(0.0001)
    hp_begin(inner_vals, nodes, weights, biases)
