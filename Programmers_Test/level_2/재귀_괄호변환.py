# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
def solution(p):
    if p == "":
        return ""
    if is_right(p):
        return p
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            u,v = p[:i+1], p[i+1:]
            if is_right(u):
                return u + solution(v)
            else:
                return "(" + solution(v) + ")" + "".join(["(" if j == ")" else ")" for j in u[1:len(u)-1]])


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



print(solution("(()())()"), "(()())()")
print(solution(")("), "()")
print(solution("()))((()"), "()(())()")
