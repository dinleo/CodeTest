from itertools import permutations


def solution(numbers):
    answer = 0
    arr = []
    for i in range(1, len(numbers) + 1):
        arr.extend(set(permutations(numbers, i)))
    for i in range(len(arr)):
        arr[i] = int("".join(arr[i]))
    arr = list(set(arr))
    for a in arr:
        if isPrime(a):
            answer += 1
    return answer


def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(solution("17"))
print(solution("011"))
