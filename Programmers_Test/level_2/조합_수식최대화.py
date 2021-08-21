from itertools import permutations
import re


def solution(expression):
    answer = 0
    oper = list(permutations(['+', '-', '*']))  # 가능한 모든 연산자 우선순위 조합
    for o in oper:
        exp_op = re.findall("\W", expression)  # 연산자만 담긴 리스트
        exp_num = re.findall("[0-9]+", expression)  # 숫자만 담긴 리스트
        s = ""
        i = 0
        # 1번 우선순위 연산자를 먼저 계산
        while i != len(exp_op):
            if o[0] == exp_op[i]:
                exp_num[i] = str(eval(exp_num[i] + o[0] + exp_num[i + 1]))
                exp_num.pop(i + 1)
                exp_op.pop(i)
            else:
                i += 1
        # 2번 우선순위 연산자를 먼저계산
        i = 0
        while i != len(exp_op):
            if o[1] == exp_op[i]:
                exp_num[i] = str(eval(exp_num[i] + o[1] + exp_num[i + 1]))
                exp_num.pop(i + 1)
                exp_op.pop(i)
            else:
                i += 1
        # 마지막 연산자를 계산
        if exp_op:
            for i in range(len(exp_op)):
                s += exp_num[i] + exp_op[i]
        s = abs(eval(s + exp_num[-1]))
        # 가장 큰 수를 answer 에 저장
        if answer < s:
            answer = s
    return answer


print(solution("100-200*300-500+20"), 60420)
print(solution("50*6-3*2"), 300)
