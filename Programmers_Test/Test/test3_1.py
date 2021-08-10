import math


def solution(n):
    n2 = n
    answer = 0
    if n2 % 2 != 0:
        n2 -= 1
    arr = [[] for i in range(int(n2 / 2) + 1)]
    for i in range(int(n2 / 2) + 1):
        for j in range(int(n2 / 2)):
            if i <= j:
                arr[i].append(1)
                arr[i].append(1)
            else:
                arr[i].append(2)
    if n % 2 != 0:
        for i in arr:
            i.append(1)

    for i in arr:
        a = i.count(1)
        b = i.count(2)
        a_b = math.factorial(a+b)
        ab = math.factorial(a) * math.factorial(b)
        answer += (a_b)//ab

    return answer%1234567


for i in range(1,12):
    print(solution(i))
