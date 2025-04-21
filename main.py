# Parametric function graph
# Jonathan Schrock
# 04/21/2025

import matplotlib.pyplot as plt
from math import sin, cos


def main():
    # Unpacks list of point tuples into two lists
    x_axis, y_axis = zip(*[x_y_of_t(t / 1000) for t in range(1, 100000)])

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_aspect("equal")
    ax.plot(x_axis, y_axis)

    plt.show()


def x_y_of_t(t: float) -> tuple:
    return (sin(t) * cos(t) ** 2) / t, (sin(t) ** 2 * cos(t)) / t


if __name__ == "__main__":
    main()
