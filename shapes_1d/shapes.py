import math

import numpy as np


def create_rectangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    vector = np.zeros(length)
    vector[position: position+width] = height
    return vector


def create_triangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    vector = np.zeros(length)
    half = np.linspace(0, height, math.ceil(width / 2))
    vector[position: position + len(half)] = half
    vector[position + width // 2: position + width] = height - half
    return vector


def create_inv_triangle(length: int, width: int, height: float, position: int) -> np.ndarray:
    vector = np.zeros(length)
    half = np.linspace(height, 0, math.ceil(width / 2))
    vector[position: position + len(half)] = half
    vector[position + width // 2: position + width] = height - half
    return vector


def create_parabola(length: int, width: int, height: float, position: int) -> np.ndarray:
    vector = np.zeros(length)
    # half = np.sqrt(1 - (np.linspace(1, 0, round(width / 2)) ** 2)) * height
    half = (1 - np.linspace(1, 0, math.ceil(width / 2)) ** 2) * height
    vector[position: position + len(half)] = half
    vector[position + width // 2: position + width] = half[::-1]
    return vector


def create_inv_parabola(length: int, width: int, height: float, position: int) -> np.ndarray:
    vector = np.zeros(length)
    half = (np.linspace(1, 0, math.ceil(width / 2)) ** 2) * height
    vector[position: position + len(half)] = half
    vector[position + width // 2: position + width] = half[::-1]
    return vector


Shapes = {
    'rectangle': create_rectangle,
    'triangle': create_triangle,
    'inv_triangle': create_inv_triangle,
    'parabola': create_parabola,
    'inv_parabola': create_inv_parabola
}
