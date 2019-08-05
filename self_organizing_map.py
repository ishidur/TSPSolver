from config import SOMConfig as Config
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import util

window_size = 5
dpi = 100
node_radius = 0.1
# b_init = 10
# b_growth = 1.005
# b_ceil = 1000

b_init = 10.0
alpha = 0.03
# b_ceil = 1000
# mu = 1.0
mu = 0.6
iter_lim = 200
record_moment = np.arange(0, iter_lim, 10)
record = True


# def g_func(djj_star, l, beta):
#     if djj_star < l:
#         return (1 - djj_star / l)**beta
#     return 0.0


def g_func(djj_star: int, l: float, g: float) -> float:
    if djj_star < l:
        return np.exp(-djj_star ** 2 / g ** 2)
    return 0.0


def calc_champ_node(band_array: np.array, city: np.array) -> int:
    dist_array = np.array([util.dist(node, city) for node in band_array])
    # find min value index
    return dist_array.argmin()


def update_node(node: np.array, city: np.array, djj_star: int, beta: float) -> np.array:
    delta_node = mu * g_func(djj_star, node_num * 0.2, beta) * (city - node)
    return delta_node


def update_band(
    band_array: np.array, city: np.array, j_star: int, beta: float
) -> np.array:
    new_band_array = band_array.copy()
    for j in range(node_num):
        djj_star = np.amin([np.abs(j - j_star), node_num - np.abs(j - j_star)])
        new_band_array[j, :] += update_node(band_array[j, :], city, djj_star, beta)
    return new_band_array


def som_begin(band_array: np.array, city_array: np.array):
    beta = b_init
    np.random.shuffle(city_array)
    if record:
        dir_name = util.make_directory(Config)
        for i in range(iter_lim):
            if i in record_moment:
                filename = "iteration-" + str(i) + ".png"
                file_path = dir_name + filename
                plt.savefig(file_path)
            picked_city = city_array[i % city_num, :]
            j_star = calc_champ_node(band_array, picked_city)
            band_array = update_band(band_array, picked_city, j_star, beta)
            circle_band = np.vstack((band_array, band_array[0, :]))
            plt.title("iteration=" + str(i + 1))
            elastic_band.set_data(circle_band[:, 0], circle_band[:, 1])
            # beta = np.amin([b_ceil, beta * b_growth])
            beta = (1 - alpha) * beta
            plt.pause(0.001)
    else:
        i = 1
        while plt.get_fignums():
            picked_city = city_array[i % city_num, :]
            j_star = calc_champ_node(band_array, picked_city)
            band_array = update_band(band_array, picked_city, j_star, beta)
            circle_band = np.vstack((band_array, band_array[0, :]))
            plt.title("iteration=" + str(i))
            elastic_band.set_data(circle_band[:, 0], circle_band[:, 1])
            i += 1
            # beta = np.amin([b_ceil, beta * b_growth])
            beta = (1 - alpha) * beta
            plt.pause(0.001)


if __name__ == "__main__":
    if Config.read_file:
        np_cities = np.genfromtxt(Config.file_path + Config.city_file, delimiter=",")
        city_num = np_cities.shape[0]
        width_x = np.max(np_cities[:, 0]) - np.min(np_cities[:, 0])
        width_y = np.max(np_cities[:, 1]) - np.min(np_cities[:, 1])
        width = np.amax([width_x, width_y])
        np_cities[:, 0] -= np.min(np_cities[:, 0])
        np_cities[:, 0] /= width
        np_cities[:, 1] -= np.min(np_cities[:, 1])
        np_cities[:, 1] /= width
        center_x = np.average(np_cities[:, 0])
        center_y = np.average(np_cities[:, 1])
        figsize = (window_size, window_size)
    else:
        city_num = Config.city_num
        # “continuous uniform” distribution random
        np_cities = np.random.random((city_num, 2))
        figsize = (window_size, window_size)
        center_x = 0.5
        center_y = 0.5

    node_num = int(city_num * 2)
    angles = np.linspace(0, 2 * np.pi, node_num)
    np_band = np.array(
        [
            node_radius * np.sin(angles) + center_x,
            node_radius * np.cos(angles) + center_y,
        ]
    ).transpose()
    fig = plt.figure(figsize=figsize, dpi=dpi)
    plt.scatter(np_cities[:, 0], np_cities[:, 1], s=20, marker="+")
    elastic_band, = plt.plot(np_band[:, 0], np_band[:, 1])
    plt.title("iteration=" + str(0))
    plt.grid()
    plt.pause(0.001)
    som_begin(np_band, np_cities)
