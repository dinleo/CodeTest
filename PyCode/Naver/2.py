# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    answer = 0
    paint = True
    layer = 0
    while paint:
        paint = False
        tic = False
        layer += 1
        for h in A:
            if not tic and layer <= h:
                tic = True
                answer += 1
                paint = True
            elif h < layer:
                tic = False
    if 1000000000 < answer:
        return -1
    return answer


def solution2(A):
    answer = A[-1]
    last_h = A[0]
    for h in A:
        gap = last_h - h
        if 0 < gap:
            answer += gap
        last_h = h
    return answer

print(solution2([1,3,2,1,2,1,5,3,3,4,2]))
print(solution2([5,8]))
print(solution2([8,1,1,1,5]))
