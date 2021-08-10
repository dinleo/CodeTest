def solution(operations):
    q = []
    answer =[]
    for i in operations:
        op = list(i.split(" "))
        if op[0] == "I":
            q.append(int(op[1]))
        if op[0] == "D" and q != []:
            if op[1] == "1":
                m = max(q)
            else:
                m = min(q)
            q.remove(m)
    if q == []:
        answer =[0,0]
    else:
        answer = [max(q),min(q)]
    return answer


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))