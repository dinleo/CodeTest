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

    def len(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

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

    def get(self, x):
        current = self.head
        i = 0
        while current != None:
            if current.data == x:
                return i
            current = current.next
            i += 1
        return False

    def has(self, x):
        current = self.get(x)
        if current != False:
            return True
        return False

    def delete(self, x):
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

    def rotate(self):
        current = self.head
        if current is None:
            return
        tNode = current
        while (current.next is not None):
            current = current.next
        current.next = self.head
        self.head = tNode.next
        tNode.next = None

def solution(n, k, cmd):
    arr = [True for _ in range(n)]
    cur = k
    cur_del = []
    for c in cmd:
        if c[0] == "U":
            u = int(c[-1])
            for i in range(cur - 1, -1, -1):
                if arr[i]:
                    u -= 1
                if u == 0:
                    cur = i
                    break
        elif c[0] == "D":
            d = int(c[-1])
            for i in range(cur + 1, n):
                if arr[i]:
                    d -= 1
                if d == 0:
                    cur = i
                    break
        elif c == "C":
            arr[cur] = False
            cur_del.append(cur)
            temp_cur = cur
            for i in range(cur + 1, n):
                if arr[i]:
                    cur = i
                    break
            if cur == temp_cur:
                for i in range(cur - 1, -1, -1):
                    if arr[i]:
                        cur = i
                        break
        else:
            arr[cur_del.pop()] = True

    answer = "".join(['O' if i else 'X' for i in arr])
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
