# https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3

def solution(n, k, cmd):
    arr = ["O" for _ in range(n)]
    cur = k
    cur_del = []
    last = n-1
    for c in cmd:
        if c[0] == "U":
            u = int(list(c.split(" "))[-1])
            cur -= u
            cur -= arr[cur:cur + u].count("X")
        elif c[0] == "D":
            d = int(list(c.split(" "))[-1])
            cur += d + arr[cur+1:cur+d+1].count("X")
        elif c == "C":
            arr[cur] = "X"
            cur_del.append(cur)
            if cur == last:
                while arr[cur] == "X":
                    cur -= 1
                last = cur
            else:
                while arr[cur] == "X":
                    cur += 1
        else:
            p = cur_del.pop(-1)
            arr[p] = "O"

    return "".join(arr)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(8,0,["C","C","C","C","C","C","C"]))
print(solution(8,7,["C","C","C","C","C","C","C"]))