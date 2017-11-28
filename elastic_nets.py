import arrayfire as af
import numpy as np
import matplotlib.pyplot as plt

af.info()

# parameters
city_num = 10
node_num = int(city_num * 2.5 + 0.5)
node_radius = 0.1
iter_lim = 100000

np_cities = np.random.random((city_num, 2))
angles = np.linspace(0, 2 * np.pi, node_num)
np_circles = np.array([node_radius * np.sin(angles) + 0.5, node_radius * np.cos(angles) + 0.5]).transpose()
print(np_cities.shape)
print(np_circles.shape)
# af_cities = af.Array(np_cities.ctypes.data, np_cities.shape, np_cities.dtype.char)
# af.display(af_cities)
fig = plt.figure(figsize=(5, 5))
plt.scatter(np_cities[:, 0], np_cities[:, 1])
elastic_band, = plt.plot(np_circles[:, 0], np_circles[:, 1])
plt.grid()
plt.xlim(0, 1)
plt.ylim(0, 1)
while True:
    np_circles[:, 0] += 0.01
    np_circles[:, 1] += 0.01
    elastic_band.set_data(np_circles[:, 0], np_circles[:, 1])
    plt.pause(0.5)
