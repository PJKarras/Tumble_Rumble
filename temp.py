import numpy as np


if __name__ == "__main__":
    displayH = 10
    displayW = 10

    mine = np.zeros((4,4))
    print("Before change of mine[0,1]:\n", mine)
    mine[0,1] = 1
    print("After change of mine[0,1]:\n", mine)
    print("Access of mine[0,1]:", mine[0,1])