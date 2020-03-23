import random


def compute(word):
    precomputed_reverse = [0, 2, 1, 3]
    bit_mask = 3
    result = 0
    max_bits = 64
    for i in range(0, max_bits, 2):
        result = (result << 2) | precomputed_reverse[(word & bit_mask)]
        word = word >> 2
    return result


input_num = random.randint(0, 2**64)

print(f'{input_num} : {compute(input_num)}')

print(compute(compute(input_num)) == input_num)
