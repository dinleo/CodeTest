def solution(x, y):
    answer = -1

    dots = []
    for i in range(len(x)):
        dots.append([x[i], y[i]])
    dots.sort(key=lambda k: k[0])
    dots.sort(key=lambda k: k[1])

    pairs = []
    i = 0
    while i < len(dots):
        i_y = dots[i][1]
        arr = [0, 0]
        j = i + 1
        while j < len(dots):
            if dots[j][1] == i_y:
                arr[0] = dots[i]
                arr[1] = dots[j]
                j += 1
            else:
                break
        if arr != [0,0]:
            pairs.append(arr)
        i = j

    p = len(pairs)
    if p<2:
        return 0
    for i in range(p):
        for j in range(i+1, p):
            a = pairs[i][1][0] - pairs[i][0][0]
            b = pairs[j][1][0] - pairs[j][0][0]
            h = pairs[j][0][1] - pairs[i][0][1]
            s = (a+b)*h
            if answer < s:
                answer = s

    return answer


print(solution([2,3,4,4,7,6,3,9,9,6,5,8,6,4], [5,9,5,1,3,1,3,3,8,7,10,9,9,8]))
