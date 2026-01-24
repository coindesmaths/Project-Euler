def probleme0006():
    """
    Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.
    """
    diff2 = 0
    for i in range(1, 100 + 1):
        for j in range(i + 1, 100 + 1):
            diff2 += 2 * i * j
    return diff2
