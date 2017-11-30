from config import GifMakerConfig as Config
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob


def sort_rule(x):
    return int(x.split('-')[1].split('.')[0])


source_dir = Config.source_dir
fig = plt.figure()
file_names = glob.glob(source_dir + "*.png")
file_names = sorted(file_names, key=sort_rule)

ims = []
for file_name in file_names:
    img = plt.imread(file_name)
    im = plt.imshow(img)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims)
ani.save(source_dir + 'animation.gif', writer="imagemagick")
# plt.show()
