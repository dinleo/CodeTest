from collections import defaultdict

def solution(value, projects):
    v = dict()
    for i in range(len(value)):
        v[str(i+1)] = value[i]

    g = defaultdict(list)
    for p in projects:
        g[str(p[0])].append(str(p[1]))

    def combine_node(node):
        if node not in g.keys():
            return v[node]
        arr = g[node]
        maxima = 0
        for i in arr:
            val = combine_node(i)
            if maxima < val:
                maxima = val
        return v[node] + maxima

    return combine_node('1')


print(solution([10, 11, 8, 5, 9, 15, 17], [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [4, 7]]))
