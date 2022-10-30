# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
def solution(name):
    answer = 0
    n = len(name)

    # 조이스틱 위아래 처리
    alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for j in range(n):
        answer += min(alp.index(name[j]), 26 - alp.index(name[j]))

    # 조이스틱 좌우 처리
    a = ["A" for _ in range(n)]
    name = list(name)
    i = 0
    while 1:
        name[i] = "A"
        if name == a:
            break
        j = 1
        while 1:
            if n <= i+j:
                if name[i+j-n] != "A":
                    i = i+j-n
                    answer += j
                    break
            else:
                if name[i+j] != "A":
                    i = i+j
                    answer += j
                    break
            if name[i-j] != "A":
                i = i-j
                answer += j
                break
            j += 1

    return answer



print(solution("JAN"))
print(solution("JEROEN"))
print(solution("BBBBBB"))
