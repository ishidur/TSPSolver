import elastic_nets as en
import self_organizing_map as som
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

window_size = 5
dpi = 100


def plot_en():
    x_min, x_max = 0.0, 1.0
    k = 0.2
    figsize = (window_size, window_size)
    x = np.linspace(x_min, x_max, 1000)
    y = en.phi(x, k)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(x, y)
    plt.xlabel("distance")
    plt.grid()
    plt.show()


def plot_som():
    x_min, x_max = -10.0, 10.0
    g = 10
    figsize = (window_size * 1.618, window_size)
    X = np.linspace(x_min, x_max, 1000)
    Y = np.array([som.g_func(np.abs(x - 0), x_max * 2, g) for x in X])
    fig = plt.figure(figsize=figsize, dpi=dpi)
    plt.plot(X, Y)
    plt.xlabel("$|j-{j}^{*}|$")
    plt.xticks(np.arange(x_min, x_max + 1, 1))
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # plot_en()
    plot_som()
