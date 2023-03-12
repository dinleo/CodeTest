def solution(low, high, img):
    i_len = len(img)
    j_len = len(img[0])
    answer = 0

    def verify(n, k):
        x = (100 * k) / (n - 2) ** 2
        if low <= x < high:
            return True
        else:
            return False

    def find_square(i, j):
        square = []
        x = 1
        while img[i][j + x] == '#' and img[i + x][j] == '#':
            if 2 <= x:
                y = 1
                while img[i + y][j + x] == '#' and img[i + x][j + y] == '#':
                    if y == x:
                        square.append(1 + x)
                        break
                    y += 1
            if i + x + 1 == i_len or j + x + 1 == j_len:
                break
            x += 1
        return square

    def count_black(i, j, n):
        k = 0
        for ii in range(i + 1, i + n - 1):
            for jj in range(j + 1, j + n - 1):
                if img[ii][jj] == '#':
                    k += 1
        return k

    for i in range(i_len - 2):
        for j in range(j_len - 2):
            if img[i][j] == '#':
                square = find_square(i, j)
                if square:
                    for s in square:
                        k = count_black(i, j, s)
                        if verify(s, k):
                            answer += 1

    return answer


print(solution(25, 51, [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))