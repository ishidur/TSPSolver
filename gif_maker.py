from config import GifMakerConfig as Config
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.animation as animation  # type: ignore
import glob

window_size = 5
dpi = 150


def sort_rule(x):
    return int(x.split("-")[1].split(".")[0])


if __name__ == "__main__":
    source_dir = Config.source_dir
    file_names = glob.glob(source_dir + "*.png")
    file_names = sorted(file_names, key=sort_rule)
    figsize = (window_size, window_size)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = plt.subplot(1, 1, 1)
    ax.spines["right"].set_color("None")
    ax.spines["top"].set_color("None")
    ax.spines["left"].set_color("None")
    ax.spines["bottom"].set_color("None")
    ax.tick_params(axis="x", which="both", top="off", bottom="off", labelbottom="off")
    ax.tick_params(axis="y", which="both", left="off", right="off", labelleft="off")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ims = []
    for file_name in file_names:
        img = plt.imread(file_name)
        im = plt.imshow(img, interpolation="spline36")
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims)
    # ani.save(source_dir + 'animation.gif', writer='imagemagick')
    plt.show()
