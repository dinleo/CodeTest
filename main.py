import heapq

arr = [[1,1,1]]
heapq.heappush(arr,[2,0,0])
heapq.heappush(arr,[3,0,1])
heapq.heappush(arr,[4,1,0])

print(heapq.heappop(arr))
print(heapq.heappop(arr))
print(heapq.heappop(arr))