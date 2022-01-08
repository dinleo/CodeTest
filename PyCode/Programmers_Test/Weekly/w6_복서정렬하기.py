# https://programmers.co.kr/learn/courses/30/lessons/85002?language=python3
def solution(weights, head2head):
    w = len(weights)
    arr = [[0,0,weights[i],-(i+1)] for i in range(w)]
    for i in range(w):
        win = head2head[i].count("W")
        lose = head2head[i].count("L")
        if win + lose:
            arr[i][0] = win/(win+lose)
    for i in range(w):
        for j in range(w):
            if head2head[i][j] == "W":
                if weights[i] < weights[j]:
                    arr[i][1] += 1

    arr.sort(reverse=True)
    answer = []
    for i in range(w):
        answer.append(arr[i][3]*(-1))
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
