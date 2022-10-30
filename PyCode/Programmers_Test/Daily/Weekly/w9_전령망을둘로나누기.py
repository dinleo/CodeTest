# https://programmers.co.kr/learn/courses/30/lessons/86971?language=python3

def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        w1 = []
        is_append = [0 for _ in range(len(wires))]
        w1.append(1)
        check = 1

        while check:
            check = 0
            for j in range(len(wires)):
                if i == j or is_append[j]:
                    continue
                if wires[j][0] in w1:
                    w1.append(wires[j][1])
                    is_append[j] = 1
                    check = 1
                elif wires[j][1] in w1:
                    w1.append(wires[j][0])
                    is_append[j] = 1
                    check = 1

        if abs(2*len(w1) - n) < answer:
            answer = abs(2*len(w1) - n)

    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))