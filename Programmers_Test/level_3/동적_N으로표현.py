def solution(NUM, number):
    arr = [[]] + [[int(str(NUM) * i)] for i in range(1,9)]

    if [number] in arr:
        return arr.index([number])

    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i-j]:
                    arr[i].append(a + b)
                    arr[i].append(a * b)
                    arr[i].append(a - b)
                    if 0 != b:
                        arr[i].append(a // b)
        if number in arr[i]:
            return i
        arr[i] = list(set(arr[i]))

    return -1

print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)