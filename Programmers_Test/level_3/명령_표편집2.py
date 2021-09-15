# https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = None
        for d in list(data)[::-1]:
            self.push(d)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        head = self.head
        if not head:
            return []
        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.data)
            pointer = pointer.next
        return sll_list

    def pop(self, x):
        temp = self.head
        if (temp is not None):
            if (temp.data == x):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == x:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None


def solution(n, k, cmd):
    arr = [i for i in range(n)]
    cur = k
    cur_del = []
    for c in cmd:
        if c[0] == "U":
            cur -= (int(c[-1]) + bisect.bisect_left(cur_del, cur))
        elif c[0] == "D":
            cur += (int(c[-1]) + len(cur_del) - bisect.bisect_left(cur_del, cur))
        elif c == "C":
            bisect.insort_left(cur)
            cur += 1
        else:
            p = cur_del.pop()
            bisect.insort_left(arr, p)
            if p < arr[cur]:
                cur += 1
    answer = ["O"]*n
    for i in cur_del:
        answer[i] = "X"
    return "".join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
