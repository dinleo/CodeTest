import math


def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    for i in range(len(numbers)):
        n = numbers[i]
        b = format(n, 'b')

        ceil = 1
        while ceil <= len(b):
            ceil *= 2
        dummy_end_leaf = ceil - len(b) - 1
        if 2 <= dummy_end_leaf:
            continue
        elif dummy_end_leaf == 1:
            b = '0' + b

        if is_possible(b):
            answer[i] = 1
    return answer


def is_possible(bin_str):
    if len(bin_str) == 1:
        return True
    mid_idx = int((len(bin_str) + 1) / 2) - 1

    a = bin_str[:mid_idx]
    mid = bin_str[mid_idx]
    b = bin_str[mid_idx + 1:]
    if mid == '0':
        return False
    else:
        return is_possible(a) & is_possible(b)


print(solution([7, 5, 31, 62, 63, 111, 95, 126, 127, 128, 129, 255]))
