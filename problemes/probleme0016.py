def probleme0016():
    n = 2
    p = 1000
    power = n**p
    result = 0
    while power != 0:
        result += power % 10
        power = power // 10
    return result
