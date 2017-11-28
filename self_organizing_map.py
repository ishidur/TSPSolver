from config import SOMConfig as config
import numpy as np
import matplotlib.pyplot as plt

window_size = 5
dpi = 150
node_radius = 0.1
iter_lim = 10000
k_init = 0.2
k_decay = 0.99
alpha = 0.2
beta = 2.1

if (config.read_file):
    np_cities = np.genfromtxt(config.city_file, delimiter=',')
    city_num = np_cities.shape[0]
    width_x = (np.max(np_cities[:, 0]) - np.min(np_cities[:, 0]))
    width_y = (np.max(np_cities[:, 1]) - np.min(np_cities[:, 1]))
    np_cities[:, 0] -= np.min(np_cities[:, 0])
    np_cities[:, 0] /= width_x * 1.1
    np_cities[:, 1] -= np.min(np_cities[:, 1])
    np_cities[:, 1] /= width_y * 1.1
    figsize = (window_size, window_size * width_y / width_x)
else:
    city_num = config.city_num
    np_cities = np.random.random((city_num, 2))
    figsize = (window_size, window_size)

node_num = int(city_num * 2.5 + 0.5)
angles = np.linspace(0, 2 * np.pi, node_num)
np_band = np.array(
    [node_radius * np.sin(angles) + 0.5, node_radius * np.cos(angles) + 0.5]).transpose()
fig = plt.figure(figsize=figsize, dpi=dpi)
plt.scatter(np_cities[:, 0], np_cities[:, 1], s=20, marker='+')
elastic_band, = plt.plot(np_band[:, 0], np_band[:, 1])
plt.grid()

# plt.xlim(0, 1)
# plt.ylim(0, 1)


def phi(distance, k):
    return np.exp(-distance ** 2 / (2 * k) ** 2)


def dist(x, y):
    return np.linalg.norm(x - y)


def calc_dist_matrix(band_array, city_array):
    dist_matrix = np.array([[dist(node, city) for node in band_array] for city in city_array])
    return dist_matrix


def calc_weight_matrix(band_array, k):
    dist_matrix = calc_dist_matrix(band_array, np_cities)
    weight_matrix = phi(dist_matrix, k)
    for city_i in range(city_num):
        sum = np.sum(weight_matrix[city_i, :])
        weight_matrix[city_i, :] /= sum
    return weight_matrix


def update_node(band_array, index, weights):
    back_i = (index - 1) % node_num
    forward_i = (index + 1) % node_num
    attraction_force = np.zeros(2)
    for city_i in range(city_num):
        attraction_force += weights[city_i, index] * (np_cities[city_i, :] - band_array[index, :])
    delta_node = alpha * attraction_force + beta * k * (
        band_array[forward_i, :] - 2 * band_array[index, :] + band_array[back_i, :])
    return delta_node


def update_band(band_array, weights):
    new_band_array = band_array.copy()
    for i in range(node_num):
        new_band_array[i, :] += update_node(band_array, i, weights)
    return new_band_array


if __name__ == "__main__":
    k = k_init
    # for i in range(iter_lim):
    while True:
        k = np.amax([0.01, k * k_decay])
        weights = calc_weight_matrix(np_band, k)
        np_band = update_band(np_band, weights)
        circle_band = np.vstack((np_band, np_band[0, :]))
        elastic_band.set_data(circle_band[:, 0], circle_band[:, 1])
        plt.pause(.01)
