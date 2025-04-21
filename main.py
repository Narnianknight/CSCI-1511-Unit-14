# Parametric function graph
# Jonathan Schrock
# 04/21/2025

import matplotlib.pyplot as plt
from math import sin, cos


def main():
    x_axis, y_axis = zip(*[x_y_of_t(t / 100) for t in range(1, 1000)])

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)

    plt.show()


def x_y_of_t(t):
    return (sin(t) * cos(t) ** 2) / t, (sin(t) ** 2 * cos(t)) / t


if __name__ == "__main__":
    main()
