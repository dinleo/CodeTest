# https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3
def solution(numbers):
    answer = []
    for n in numbers:
        i = n+1
        p = 0
        while 2 < (bin(n ^ i).count("1")):
            i += 2**p
            p += 1
        answer.append(i)
    return answer


print(solution([2, 7]))
