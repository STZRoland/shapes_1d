from pathlib import Path
import sys

import numpy as np
import pandas as pd

from shapes_1d.shapes import Shapes

LENGTH = 100
WIDTH_RANGE = (10, 30, 1)
HEIGHT_RANGE = (0.5, 1.05, 0.05)
POSITION_RANGE = (0, 70, 2)


def create_dataset(save_folder: Path):
    if not save_folder.is_dir():
        raise AttributeError(f'{save_folder} is not an existing directory.')

    shapes = [shape for shape in Shapes.keys()]
    widths = np.arange(*WIDTH_RANGE)
    heights = np.arange(*HEIGHT_RANGE)
    positions = np.arange(*POSITION_RANGE)

    widths_labels = np.linspace(0, 1, len(widths))
    heights_labels = np.linspace(0, 1, len(heights))
    positions_labels = np.linspace(0, 1, len(positions))

    n_samples = len(widths) * len(heights) * len(positions) * len(shapes)

    print(f'Number of shapes: {len(shapes)}')
    print(f'Number of widths: {len(widths)}')
    print(f'Number of heights: {len(heights)}')
    print(f'Number of positions: {len(positions)}')
    print(f'Total number of samples" {n_samples}')
    print()

    data = np.zeros((n_samples, LENGTH))
    labels_s = [None] * n_samples
    labels_w = [None] * n_samples
    labels_h = [None] * n_samples
    labels_p = [None] * n_samples

    i = 0
    for s in shapes:
        for w_idx, w in enumerate(widths):
            for h_idx, h in enumerate(heights):
                for p_idx, p in enumerate(positions):
                    data[i] = Shapes[s](LENGTH, w, h, p)
                    labels_s[i] = s
                    labels_w[i] = widths_labels[w_idx]
                    labels_h[i] = heights_labels[h_idx]
                    labels_p[i] = positions_labels[p_idx]
                    i += 1

    assert i == n_samples
    assert None not in labels_s
    assert None not in labels_w
    assert None not in labels_h
    assert None not in labels_p

    labels = pd.DataFrame({
        'shape': labels_s,
        'width': labels_w,
        'height': labels_h,
        'position': labels_p,
    })

    np.save(str(save_folder.joinpath('data.npy')), data)
    labels.to_csv(save_folder.joinpath('labels.csv'))

    with open(save_folder.joinpath('labels_possible_values.txt'), 'w') as f:
        label_ranges = {
            'shape': list(shapes),
            'width': list(widths_labels),
            'height': list(heights_labels),
            'position': list(positions_labels),
        }
        f.write(str(label_ranges))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        path = Path(Path.cwd())

    create_dataset(path)
