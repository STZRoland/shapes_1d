import math

import numpy as np


def _get_start_end(position, width):
    return position - math.floor(width / 2), math.ceil(position + width / 2)


def _create_vector(half_1, half_2, width, position, length):
    vector = np.zeros(length)
    if width % 2 == 1:
        half_1 = half_1[:-1]

    start, end = _get_start_end(position, width)
    assert end - start == width

    vector[start: position] = half_1
    vector[position: end] = half_2

    return vector

