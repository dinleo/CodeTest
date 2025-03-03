def solution(A):
    A = sorted(list(set(A)))
    print(A)
    i = 0
    for a in range(len(A)):
        if a<0:
            continue
        else:
            i = a
    nA = A[i:]
    print(nA)
    answer = 1
    for a in nA:
        if a==answer:
            answer += 1
        else:
            return answer
