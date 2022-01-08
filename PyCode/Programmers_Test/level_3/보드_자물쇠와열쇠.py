# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
def solution(key, lock):
    def rotate_90(matrix):
        # 시계방향으로 90도 회전한 matrix 를 반환
        ret = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                ret[c][n - 1 - r] = matrix[r][c]
        return ret

    # lock 에서 홈이 있는 최소 최대 i,j 를 찾는다. (= 검사지역)
    n = len(key)
    m = len(lock)
    min_i, min_j, max_i, max_j = m, m, -1, -1
    for i in range(m):
        for j in range(m):
            if not lock[i][j]:
                if i < min_i: min_i = i
                if j < min_j: min_j = j
                if max_i < i: max_i = i
                if max_j < j: max_j = j

    lock_i, lock_j = max_i - min_i + 1, max_j - min_j + 1

    # 구멍이 없으면 T 반환
    if max_i == -1:
        return True
    # 열쇠의 최소크기를 만족하지 못하면 F 반환
    if n < lock_i or n < lock_j:
        return False


    for _ in range(4):
        for i in range(n - lock_i + 1):
            for j in range(n - lock_j + 1):
                # 검사지역에서 열쇠와 비교할 부분을 temp_lock 에 담는다.
                # 만약 검사지역이 2x2크기이고, 열쇠의 크기가 4x4라면, lock[min_i-2][min_j-2] ~ lock[max_i+2][max_j+2] 의 범위내에서 4x4 를 담아 9번 시행된다.
                # 단, lock 범위를 벗어나면 담지않는다.
                temp_lock = [arr[max(0, max_j - n + 1 + j):min(m, max_j + j + 1)] for arr in
                             lock[max(0, max_i - n + 1 + i):min(m, max_i + i + 1)]]
                t_i, t_j = len(temp_lock), len(temp_lock[0])
                # temp_lock 의 크기가 key 의 크기와 다를때, 보정값
                if max_i+1 < n:
                    i_gap = n-t_i
                else:
                    i_gap = 0
                if max_j+1 < n:
                    j_gap = n-t_j
                else:
                    j_gap = 0

                # 조건을 만족하면 True 를 반환
                is_open = True
                for ii in range(t_i):
                    for jj in range(t_j):
                        if not key[ii+i_gap][jj+j_gap] ^ temp_lock[ii][jj]:
                            is_open = False
                if is_open:
                    return True
        key = rotate_90(key)

    return False

#
# print(solution([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
#                [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 1], [1, 1, 1, 1, 1]]))
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 0]],[[0, 1, 1], [1, 0, 1], [1, 1, 1]]))