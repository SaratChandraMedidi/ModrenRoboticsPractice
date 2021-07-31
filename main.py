import numpy as np
import modern_robotics as mr
R = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]])
invR = mr.RotInv(R)
help(mr.RotInv)
print("Working!")