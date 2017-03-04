from src.ForestGrid import *
import matplotlib.pyplot as plotter
import matplotlib.colors as col
import matplotlib.animation as animation


def main():
    grid_size = 1000
    growth_probability = 0.01
    fire_probability = 0.0001

    forest = ForestGrid(grid_size, growth_probability, fire_probability)

    fig = plotter.figure()

    cmap = col.ListedColormap(["k", "g", "r"])
    bounds = [-0.5, 0.5, 1.5, 2.5]
    norm = col.BoundaryNorm(bounds, cmap.N)

    ax = fig.add_subplot(111, aspect='equal')
    image = ax.imshow(forest.values, cmap=cmap, norm=norm, animated=True)

    def init():
        image.set_data(forest.values)
        return image,

    def animate(i):
        forest.process_cells()
        image.set_data(forest.values)
        return image,

    ani = animation.FuncAnimation(fig, animate, frames=600, interval=50, blit=True, init_func=init)
    ani.save('basic_animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

    plotter.show()


if __name__ == "__main__": main()
