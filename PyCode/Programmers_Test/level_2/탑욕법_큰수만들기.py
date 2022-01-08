# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
def solution(number, k):
    answer = ""
    n = number
    # n[0]을 뺀 후, 조건에 부합하면 스택에 쌓고, 아니면 버리는 알고리즘
    len_result = len(n)-k
    stack = ""
    i = 0
    while k != 0 and i < len(n):
        # 스택이 비어있으면 무조건 push
        if stack == "":
            stack += n[i]
            i += 1
        # 스택의 top 보다 n[0]이 크면 스택의 top을 지우고 k -1
        elif stack[-1] < n[i]:
            stack = stack[:-1]
            k -= 1
        # 아닌경우 그냥 push
        else:
            stack += n[i]
            i += 1
    # 남은 문자열을 answer에 모두 추가
    stack += n[i:]
    # 모두 동일한 숫자로 이루어져있을때의 처리
    answer = stack[:len_result]
    return answer