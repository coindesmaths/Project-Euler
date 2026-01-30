from utils.data import Data


def probleme0018():
    triangle = Data.init(18)
    triangle = [[int(j) for j in i.split()] for i in triangle.split("\n")]
    triangle.reverse()
    for i in range(1, len(triangle)):
        for j, k in enumerate(triangle[i]):
            triangle[i][j] = k + max([triangle[i - 1][j], triangle[i - 1][j + 1]])
    result = triangle[-1][0]
    return result
