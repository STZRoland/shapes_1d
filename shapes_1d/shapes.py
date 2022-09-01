import math

import numpy as np

from shapes_1d.utils import _create_vector


def create_rectangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    half_1 = np.ones(math.ceil(width / 2)) * height
    half_2 = np.ones_like(half_1) * height
    return _create_vector(half_1, half_2, width, position, length)


def create_triangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    half_1 = np.linspace(0, height, math.ceil(width / 2))
    half_2 = height - half_1
    return _create_vector(half_1, half_2, width, position, length)


def create_inv_triangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    half_1 = np.linspace(height, 0, math.ceil(width / 2))
    half_2 = height - half_1
    return _create_vector(half_1, half_2, width, position, length)


def create_half_circle(length: int, width: int, height: float, position: int) -> np.ndarray:
    half_1 = np.sqrt(1 - (np.linspace(1, 0, math.ceil(width / 2)) ** 2)) * height
    half_2 = half_1[::-1]
    return _create_vector(half_1, half_2, width, position, length)


def create_inv_half_circle(length: int, width: int, height: float, position: int) -> np.ndarray:
    half_1 = (1 - np.sqrt(1 - (np.linspace(1, 0, math.ceil(width / 2)) ** 2))) * height
    half_2 = half_1[::-1]
    return _create_vector(half_1, half_2, width, position, length)


Shapes = {
    'rectangle': create_rectangle,
    'triangle': create_triangle,
    'inv_triangle': create_inv_triangle,
    'half_circle': create_half_circle,
    'inv_half_circle': create_inv_half_circle
}
