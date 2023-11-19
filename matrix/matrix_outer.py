import numpy as np
from icecream import ic

a = np.array(([64,4]))#, [2,4,5], [8,7,9]))
# b = np.array(([4,5,6]))#, [2,1,1], [1,1,9]))

# ic(np.add.outer(a, a))

b = np.array(([4,7,9]))
# ic(a)
ic(np.sum(a, axis=1))
