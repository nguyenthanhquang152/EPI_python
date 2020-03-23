def compute(word, i, j):
    if (word >> i) & 1 != (word >> j) & 1:
        mask = 0
        mask |= 1 << i
        mask |= 1 << j
        return word ^ mask
    return word


print(compute(73, 1, 6))
