import heapq

city = {'a': {'b': 5, 'c': 4},
        'b': {'a': 5, 'c': 5, 'd': 7, 'e': 6},
        'c': {'a': 4, 'b': 5, 'd': 3, 'e': 8},
        'd': {'b': 7, 'c': 3, 'f': 3},
        'e': {'b': 6, 'c': 8, 'g': 3},
        'f': {'d': 3, 'g': 2},
        'g': {}}
cityEuclid = {'a': 0, 'b': 8, 'c': 7, 'd': 4, 'e': 3, 'f': 2, 'g': 0}


def search(search_type):
    open_list = [[0, 'a']]
    close_list = []
    while not len(open_list) == 0:
        arr = heapq.heappop(open_list)
        path_cost = arr[0]
        path = arr[1]
        node = path[-1]

        close_list.append(node)

        if node == 'g':
            return '\n<find!>\npath: ' + path + '\ncost: ' + str(path_cost)

        for n in city[node]:
            if n not in close_list:
                is_in = False
                # just put 'BFS' or ... in get_cost(param1)
                next_cost = get_cost(search_type, path_cost, node, n)
                for o in open_list:
                    if o[1][-1] == n:
                        if next_cost < o[0]:
                            open_list.remove(o)
                        else:
                            is_in = True
                        break
                if not is_in:
                    heapq.heappush(open_list, [next_cost, path + n])

        print('[' + node + ']  - ', end='')
        print(open_list)

    return 'fail'


def get_cost(search_type, path_cost, cur_node, next_node):
    if search_type == 'BFS':
        return path_cost + 1
    elif search_type == 'UCS':
        return path_cost + city[cur_node][next_node]
    elif search_type == 'GBS':
        return cityEuclid[next_node]
    elif search_type == 'A_S':
        return path_cost + city[cur_node][next_node] - cityEuclid[cur_node] + cityEuclid[next_node]


print('=========BFS=========\nnode - [cost, path]')
print(search('BFS'))
print('\n=========UCS=========\nnode - [cost, path]')
print(search('UCS'))
print('\n=========GBS=========\nnode - [cost, path]')
print(search('GBS'))
print('\n=========A_S=========\nnode - [cost, path]')
print(search('A_S'))
