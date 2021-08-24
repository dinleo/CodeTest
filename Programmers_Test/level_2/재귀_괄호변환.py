# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
# 나도 알아보지 못 할 재귀 알고리즘. 다시 깔끔하게 재도전. 함수를 줄여보자.

def solution(p):
    if p == "":
        return ""
    if is_right(p):
        return p
    answer = ""
    u = p
    while 1:
        u, v = get_uv(u)
        if is_right(u):
            answer += u
            u = v
            continue
        else:
            break
    answer += "(" + solution(v) + ")" + u_strip(u)

    return answer


def get_uv(s):
    l_count = 0
    r_count = 0
    for i in range(len(s)):
        if s[i] == '(':
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            return s[:i + 1], s[i + 1:]


def is_right(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True


def u_strip(s):
    new_u = ""
    for i in range(1,len(s)-1):
        if s[i] == '(':
            new_u += ')'
        else:
            new_u += '('
    return new_u


print(solution("(()())()"), "(()())()")
print(solution(")("), "()")
print(solution("()))((()"), "()(())()")
