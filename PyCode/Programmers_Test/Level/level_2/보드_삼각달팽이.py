# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
def solution(n):
    left,right,top,bot = 0,-1,1,n-1
    down = True
    arr = [[0 for _ in range(i)] for i in range(1,n+1)]
    j = 0
    k = 0
    for i in range(1,n*(n+1)//2+1):
        if down:
            if j != bot:
                arr[j][left] = i
                j += 1
                continue
            else:
                if k != j+right+1:
                    arr[j][k] = i
                    k += 1
                    continue
                else:
                    arr[j][k] = i
                    left += 1
                    bot -= 1
                    k = left
                    j -= 1
                    down = False
                    continue
        else:
            if j != top:
                arr[j][right] = i
                j -= 1
                continue
            else:
                arr[j][right] = i
                right -= 1
                top += 2
                j += 1
                down = True
    answer = []
    for a in arr:
        answer.extend(a)
    return answer


print(solution(6))