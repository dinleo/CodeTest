import heapq


def solution(p, q):
    def merge(x, y):
        heapq.heapify(x)
        heapq.heapify(y)
        while x != y:
            if len(x) == len(y):
                return False
            while x and y and x[0] == y[0]:
                heapq.heappop(x)
                heapq.heappop(y)

        return True

    answer = []
    for i in range(len(p)):
        answer.append(merge(p[i], q[i]))

    return answer


print(solution([[4, 3, 3], [1, 2, 3], [3, 2, 4]], [[5, 5], [5, 1], [1, 8]]))
