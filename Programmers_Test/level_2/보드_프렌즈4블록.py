# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3
def solution(m, n, board):
    def pop_blocks():
        # 보드를 검사해 블럭을 터뜨린 후, 터뜨린 블럭 갯수를 반환하는 함수
        count = 0
        blocks_pop = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    blocks_pop.append([i, j])
        for b in blocks_pop:
            for i in range(2):
                for j in range(2):
                    if board[b[0]+i][b[1]+j]:
                        board[b[0]+i][b[1]+j] = 0
                        count += 1
        return count

    def drop_blocks():
        # 빈공간에 블럭을 떨어뜨리는 함수
        for i in range(m - 1,0,-1):
            for j in range(n):
                if not board[i][j]:
                    k = i - 1
                    while k != -1 and not board[k][j]:
                        k -= 1
                    if k == -1:
                        continue
                    else:
                        for a in range(k+1):
                            board[i-a][j] = board[k-a][j]
                            board[k-a][j] = 0

    answer = 0
    board = [[j for j in i] for i in board]
    c = 1
    while c:
        c = pop_blocks()
        answer += c
        drop_blocks()
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
