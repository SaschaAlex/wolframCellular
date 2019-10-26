# Elementary cellular automata [![Build Status](https://travis-ci.org/SaschaAlex/Laplacian-Solver.svg?branch=master)](https://travis-ci.org/SaschaAlex/Laplacian-Solver)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
An elementary cellular automata written in python 3


## Requirements
* python 3.0 + 
* matplotlib (optional)



## Installation


Clone :
```sh
git clone https://github.com/SaschaAlex/wolframCellular
```
### Code [Exemple](https://github.com/SaschaAlex/wolframCellular/blob/master/plot.py)
```python
import numpy as np
import matplotlib.pyplot as plt
from main import game
H = np.array(game(30 , 2**15 , 15))  # added some commas and array creation code

fig = plt.figure(figsize=(13, 6.2))
ax = fig.add_subplot(111)
ax.matshow(H, cmap=plt.cm.Blues)
plt.show()
```
###  Result

![](https://i.imgur.com/i5eJuYH.jpg)

## Contributing

1. Fork it (<https://github.com/SaschaAlex/wolframCellular/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request