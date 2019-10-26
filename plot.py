import numpy as np
import matplotlib.pyplot as plt
from main import game
H = np.array(game(30 , 2**15 , 15))  # added some commas and array creation code

fig = plt.figure(figsize=(13, 6.2))
ax = fig.add_subplot(111)
ax.matshow(H, cmap=plt.cm.Blues)
plt.show()
