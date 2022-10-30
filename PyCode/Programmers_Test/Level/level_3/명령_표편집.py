# https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    arr = []
    for i in range(n):
        # 이중연결리스트 생성
        node = Node("O")
        node.prev = i - 1
        node.next = i + 1
        arr.append(node)
    # head 와 tail 작업
    arr[0].prev = None
    arr[-1].next = None
    head = 0
    tail = n - 1
    cur = k
    removed_node = []

    for c in cmd:
        if c[0] == "U":
            u = int(list(c.split(" "))[-1])
            for i in range(u):
                cur = arr[cur].prev
        elif c[0] == "D":
            d = int(list(c.split(" "))[-1])
            for i in range(d):
                cur = arr[cur].next
        elif c == "C":
            if cur != tail:
                if cur != head:
                    # 일반 노드: 이전노드와 다음노드를 연결시켜준다
                    arr[arr[cur].prev].next = arr[cur].next
                    arr[arr[cur].next].prev = arr[cur].prev
                else:
                    # head: 다음노드의 prev 삭제
                    arr[arr[cur].next].prev = None
                    head = arr[cur].next
                # cur 는 다음노드를 가르킨다.
                temp = arr[cur].next
            else:
                # tail: 이전노드의 next 삭제
                arr[arr[cur].prev].next = None
                tail = arr[cur].prev
                # cur 는 이전노드를 가르킨다.
                temp = arr[cur].prev
            # kill cur node
            removed_node.append(cur)
            arr[cur].data = "X"
            arr[cur].prev = None
            arr[cur].next = None
            cur = temp
        else:
            p = removed_node.pop(-1)
            arr[p].data = "O"
            if p < head:
                # head 보다 앞의 노드가 부활
                arr[p].next = head
                arr[head].prev = p
                head = p
            elif tail < p:
                # tail 보다 뒤의 노드가 부활
                arr[p].prev = tail
                arr[tail].next = p
                tail = p
            else:
                # 일반노드 부활
                p_next = p + 1
                # 가장 인접한 살아있는 다음노드를 찾아 사이에 끼워넣는다.
                while arr[p_next].data == "X":
                    p_next += 1
                arr[p].next = p_next
                arr[p].prev = arr[p_next].prev
                arr[arr[p_next].prev].next = p
                arr[p_next].prev = p

    answer = "".join([arr[i].data for i in range(n)])
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(8,0,["C","C","C","C","C","C","C"]))
print(solution(8,7,["C","C","C","C","C","C","C"]))
print(solution(8,1,["C","C","C","C","C","U 1","C"]))