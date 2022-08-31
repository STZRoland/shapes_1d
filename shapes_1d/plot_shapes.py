import matplotlib.pyplot as plt

from shapes import *


values = (100, 21, 1.0, 50)

vector_0 = create_rectangle(*values)
vector_1 = create_triangle(*values)
vector_2 = create_inv_triangle(*values)
vector_3 = create_half_circle(*values)
vector_4 = create_inv_half_circle(*values)


fig, axs = plt.subplots(5, 1, figsize=(9, 4))
cmap = plt.get_cmap('Set1')

axs[0].plot(vector_0, c=cmap.colors[0])
axs[0].set_xticklabels([])
axs[1].plot(vector_1, c=cmap.colors[1])
axs[1].set_xticklabels([])
axs[2].plot(vector_2, c=cmap.colors[2])
axs[2].set_xticklabels([])
axs[3].plot(vector_3, c=cmap.colors[3])
axs[3].set_xticklabels([])
axs[4].plot(vector_4, c=cmap.colors[4])

plt.show()