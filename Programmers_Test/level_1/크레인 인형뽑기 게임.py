def solution(board, moves):
    answer = 0
    stack = [-1]
    for m in moves:
        for i in board:
            if i[m-1] == 0:
                pass
            elif (stack[-1] == i[m-1]):
                stack.pop()
                i[m-1] = 0
                answer += 2
                break
            else:
                stack.append(i[m-1])
                i[m-1] = 0
                break
    return answer



print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
