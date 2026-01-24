def probleme0004():
    """
    Find the largest palindrome made from the product of two (n=3)-digit numbers.
    """
    maxi, coef_maxi = 0, 0
    for i in range(1000, 0, -1):
        for j in range(i, 0, -1):
            if str(i * j) == str(i * j)[::-1]:
                maxi = max(maxi, i * j)
                coef_maxi = max(coef_maxi, i)
    return maxi
