# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
def solution(s):
    stack = [1]
    for i in s:
        if stack[-1] == i:
            stack.pop()
            print("팝",stack)
            continue
        stack.append(i)
        print("푸쉬",stack)
    if len(stack) == 1:
        return 1
    else:
        return 0



print(solution("cdcd"))
