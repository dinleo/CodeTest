# 그냥 분업 연습 해보고 싶었던 코드입니다.

def solution(game_board, table):
    answer = 0
    global N
    global g
    global t
    global m
    N = len(game_board)
    g = game_board
    t = table
    block_set_g = []
    block_set_t = []
    # board의 블럭들을 "110 010 011 " 등의 문자열로 변환해 block_set_g에 담는 알고리즘
    for i in range(N):
        for j in range(N):
            if g[i][j] == 0:
                # 최초로 0을 발견하면 m(NxN)에 블럭모양과 위치를 copy
                m = [[0 for _ in range(N)] for _ in range(N)]
                block_copy_g(i, j)
                # 90,180,270도 회전한 m2,m3,m4
                m2 = rotate_90(m)
                m3 = rotate_90(m2)
                m4 = rotate_90(m3)
                # m~m4를 자른 후 문자열로 변환해 set으로 병합 후 block_set_g에 추가
                block_set_g.append({block_cut(m),block_cut(m2),block_cut(m3),block_cut(m4)})

    # table에도 같은 작업을 반복해 block_set_t에 담는다.
    for i in range(N):
        for j in range(N):
            if t[i][j] == 1:
                m = [[0 for _ in range(N)] for _ in range(N)]
                block_copy_t(i, j)
                m2 = rotate_90(m)
                m3 = rotate_90(m2)
                m4 = rotate_90(m3)
                block_set_t.append({block_cut(m),block_cut(m2),block_cut(m3),block_cut(m4)})

    # block_g와 block_t의 겹치는 block을 발견하면 block의 크기(1의갯수)만큼 answer 증가
    for b in block_set_g:
        if b in block_set_t:
            block_set_t[block_set_t.index(b)] = {}
            answer += b.pop().count('1')



    return answer


def block_copy_g(i, j):
    # board의 block을 m에 copy
    if (i < 0) or (j < 0) or (N-1 < i) or (N-1 < j):
        return
    if g[i][j] == 1:
        return
    if g[i][j] == 0:
        m[i][j] = 1
        g[i][j] = 1
        block_copy_g(i - 1, j)
        block_copy_g(i, j - 1)
        block_copy_g(i + 1, j)
        block_copy_g(i, j + 1)


def block_copy_t(i, j):
    # table의 block을 m에 copy
    if (i < 0) or (j < 0) or (N-1 < i) or (N-1 < j):
        return
    if t[i][j] == 0:
        return
    if t[i][j] == 1:
        m[i][j] = 1
        t[i][j] = 0
        block_copy_t(i - 1, j)
        block_copy_t(i, j - 1)
        block_copy_t(i + 1, j)
        block_copy_t(i, j + 1)


def rotate_90(m):
    # 시계방향으로 90도 회전한 matrix를 반환
    global N
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]
    return ret


def block_cut(m):
    # matrix를 최소 필요한 길이의 matrix로 자름
    global N
    i1, i2, i3, i4 = 0, 0, 0, 0
    for i in range(N):
        if 1 in m[i]:
            i1 = i
            break
    for i in range(N - 1, -1, -1):
        if 1 in m[i]:
            i2 = i
            break
    j, t = 0, 0
    while t != 1:
        for i in range(N):
            if m[i][j] == 1:
                j1 = j
                t = 1
                break
        j += 1
    j, t = N - 1, 0
    while t != 1:
        for i in range(N):
            if m[i][j] == 1:
                j2 = j
                t = 1
                break
        j -= 1
    cut_m = [[m[i][j] for j in range(j1, j2 + 1)] for i in range(i1, i2 + 1)]
    # 자른 matrix를 다루기 쉽도록 문자열로 변환 ([1,1,1],[0,0,1] -> "111 001")
    s = ""
    for y in cut_m:
        for x in y:
            s += str(x)
        s += ' '
    return s


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))
