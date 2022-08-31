import numpy as np
import matplotlib.pyplot as plt

data = np.load("../data/data.npy")

plt.plot(np.mean(data, axis=0))
plt.show()
