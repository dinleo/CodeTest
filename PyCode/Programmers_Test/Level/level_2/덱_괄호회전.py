# https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3
from collections import deque


def solution(s):
    def is_right(x):
        stack = deque()
        while x:
            p = x.popleft()
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif not stack:
                return False
            elif p == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif p == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif p == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

    answer = 0
    d = deque(s)
    for i in range(len(d)):
        if is_right(d.copy()):
            answer += 1
        d.rotate()
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("([{)}]"))
print(solution("{{{"))

