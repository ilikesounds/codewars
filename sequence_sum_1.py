def sequence_sum(b, e, s):
    if b > e:
        return 0

    return sum(range(b, e + 1, s))
