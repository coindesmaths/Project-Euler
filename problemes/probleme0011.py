from utils.data import Data


def probleme0011():
    grid = Data.init(11)
    grid = list(
        map(
            lambda x: list(map(lambda n: int(n), x.split(" "))),
            grid.replace("  ", "").split("\n")[1:-1],
        )
    )

    n = 4
    maxi = 0

    horizontal_max = max(
        grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        for i in range(len(grid))
        for j in range(len(grid) + 1 - n)
    )

    vertical_max = max(
        grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        for i in range(len(grid) + 1 - n)
        for j in range(len(grid))
    )

    diagonal1_max = max(
        grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        for i in range(len(grid) + 1 - n)
        for j in range(17)
    )

    diagonal2_max = max(
        grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
        for i in range(n - 1, len(grid))
        for j in range(len(grid) + 1 - n)
    )

    max_max = max(horizontal_max, vertical_max, diagonal1_max, diagonal2_max)

    return max_max
