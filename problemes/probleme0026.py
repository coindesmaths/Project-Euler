def probleme0026():
    def cycle_length(den):
        reste = 10
        i = 0
        while reste != 10 or i < 1:
            reste = (reste % den) * 10
            i += 1
        return i

    longest = 0
    n = 1000
    for k in range(2, n + 1):
        if k % 2 != 0 and k % 5 != 0:
            length = cycle_length(k)
            if length > longest:
                longest = length
                result = k
    return result
