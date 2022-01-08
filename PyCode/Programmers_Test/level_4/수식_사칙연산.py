# https://programmers.co.kr/learn/courses/30/lessons/1843?language=python3
def solution(arr):
    max_v, min_v = "0", "0"
    while len(arr) != 1:
        # "-" 를 마주칠 때 마다 그 뒤 수식을 최댓값과 최솟값으로 간소화하며 수식을 줄여나가는 알고리즘
        for i in range(len(arr) - 2, -2, -2):
            # 뒤에서 부터 탐색해 처음으로 마주치는 "-"를 찾는다.
            if arr[i] == "-":
                if i == len(arr) - 1:
                    # 맨 마지막 연산자가 "-"라서 시작부터 마주치는 경우에만 예외처리
                    max_v = "(-" + arr[i + 1] + ")"
                    min_v = "(-" + arr[i + 1] + ")"
                    arr = arr[:i]
                    break
                else:
                    # 그 외의 경우, 찾은 "-" 부터 시작한 수식으로부터 나올 수 있는 최댓값과 최솟값을 찾은 후, arr 슬라이싱
                    values = [eval("".join(arr[i:])) + eval(max_v), (-1) * eval("".join(arr[i + 1:])) + eval(min_v),
                              (-1) * (eval("".join(arr[i + 1:])) + eval(max_v)),
                              (-1) * (eval("".join(arr[i + 1:])) + eval(min_v))]
                    arr = arr[:i]
                    max_v = "(" + str(max(values)) + ")"
                    min_v = "(" + str(min(values)) + ")"
                    break
            if i == -1:
                return eval("".join(arr + ["+", max_v]))
    return eval("".join(arr + ["+", max_v]))


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
