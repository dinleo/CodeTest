def solution(m, b):
    answer = []
    b_arr = []
    ind = 0
    for i in m:
        b_arr.append(b[ind:ind+i])
        ind += i
    for arr in b_arr:
        b = arr[0]
        for a in arr:
            b = b & a
        min_bit_length = len(b)
        for a in arr:
            if not b & a:
                pass

    return answer




print(solution([2,2],[3,2,1,2]))