import numpy

if __name__ == "__main__":
    displayH = 10
    displayW = 10

    pixelMatrix = numpy.zeros((displayH, displayW))

    currentHeight = 3
    pixelMatrix[0][0] = 5
    for index in range(displayH-1, displayH-currentHeight-1, -1):
            pixelMatrix[index][0] = 1
    print(pixelMatrix)