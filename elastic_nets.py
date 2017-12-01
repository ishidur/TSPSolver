from config import ENConfig as Config
import numpy as np
import matplotlib.pyplot as plt
import os

window_size = 5
dpi = 100
node_radius = 0.1
k_init = 0.2
k_decay = 0.99
k_bottom = 0.01
alpha = 0.2
beta = 2.1
iter_lim = 500
record_moment = np.arange(0, iter_lim, 10)
record = True


def phi(distance, k):
    return np.exp(-distance ** 2 / (2 * k) ** 2)


def dist(p1, p2):
    return np.linalg.norm(p1 - p2)


def calc_dist_matrix(band_array, city_array):
    dist_matrix = np.array([[dist(node, city)
                             for node in band_array] for city in city_array])
    return dist_matrix


def calc_weight_matrix(band_array, city_array, k):
    dist_matrix = calc_dist_matrix(band_array, city_array)
    weight_matrix = phi(dist_matrix, k)
    for city_i in range(city_num):
        sum = np.sum(weight_matrix[city_i, :])
        weight_matrix[city_i, :] /= sum
    return weight_matrix


def update_node(index, band_array, city_array, weights, k):
    back_i = (index - 1) % node_num
    forward_i = (index + 1) % node_num
    attraction_force = np.zeros(2)
    for city_i in range(city_num):
        attraction_force += weights[city_i, index] * \
                            (city_array[city_i, :] - band_array[index, :])
    delta_node = alpha * attraction_force + beta * k * (
        band_array[forward_i, :] - 2 * band_array[index, :] + band_array[back_i, :])
    return delta_node


def update_band(band_array, city_array, weights, k):
    new_band_array = band_array.copy()
    for i in range(node_num):
        new_band_array[
        i, :] += update_node(i, band_array, city_array, weights, k)
    return new_band_array


def make_directory():
    dir_name = './results/'
    directory = os.path.dirname(dir_name)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    dir_name += Config.city_file.replace(
        '.csv', '') + '/'
    directory = os.path.dirname(dir_name)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    dir_name += 'elastic_nets/'
    directory = os.path.dirname(dir_name)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    return dir_name


def en_begin(band_array, city_array):
    k = k_init
    if record:
        dir_name = make_directory()
        for i in range(iter_lim):
            if i in record_moment:
                filename = 'iteration-' + str(i) + '.png'
                file_path = dir_name + filename
                plt.savefig(file_path)
            k = np.amax([k_bottom, k * k_decay])
            weights = calc_weight_matrix(band_array, city_array, k)
            band_array = update_band(band_array, city_array, weights, k)
            circle_band = np.vstack((band_array, band_array[0, :]))
            plt.title("iteration=" + str(i + 1))
            elastic_band.set_data(circle_band[:, 0], circle_band[:, 1])
            plt.pause(.001)
    else:
        i = 1
        while plt.get_fignums():
            k = np.amax([0.01, k * k_decay])
            weights = calc_weight_matrix(band_array, city_array, k)
            band_array = update_band(band_array, city_array, weights, k)
            circle_band = np.vstack((band_array, band_array[0, :]))
            plt.title("iteration=" + str(i))
            elastic_band.set_data(circle_band[:, 0], circle_band[:, 1])
            i += 1
            plt.pause(.001)


if __name__ == "__main__":
    if (Config.read_file):
        np_cities = np.genfromtxt(
            Config.file_path + Config.city_file, delimiter=',')
        city_num = np_cities.shape[0]
        width_x = (np.max(np_cities[:, 0]) - np.min(np_cities[:, 0]))
        width_y = (np.max(np_cities[:, 1]) - np.min(np_cities[:, 1]))
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
        center_x = 0.5
        center_y = 0.5
        figsize = (window_size, window_size)

    node_num = int(city_num * 2.5 + 0.5)
    angles = np.linspace(0, 2 * np.pi, node_num)
    np_band = np.array(
        [node_radius * np.sin(angles) + center_x, node_radius * np.cos(angles) + center_y]).transpose()
    fig = plt.figure(figsize=figsize, dpi=dpi)
    plt.scatter(np_cities[:, 0], np_cities[:, 1], s=20, marker='+')
    elastic_band, = plt.plot(np_band[:, 0], np_band[:, 1])
    plt.title("iteration=" + str(0))
    plt.grid()
    plt.pause(.001)
    en_begin(np_band, np_cities)
