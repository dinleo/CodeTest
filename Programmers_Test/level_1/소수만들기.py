from itertools import combinations as cb

def solution(nums):
    answer = 0
    for i in cb(nums,3):
        if is_prime(sum(i)):
            answer += 1
    return answer


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True


print(solution([1,2,7,6,4]))
