import math


def solution(arr):
    print(math.gcd(2, 6))
    ar = arr
    ar.sort()
    answer = 1
    while ar:
        answer = lcm(answer, ar[0])
        print(answer)
        del ar[0]

    return answer


def lcm(x, y):
    return int((x * y) / (math.gcd(x, y)))


print(solution([2, 6, 8, 14]))
