
import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for n in range(N):
    x = int(input())
    if x == 0:
        if len(heap) > 1:
            if heap[0][0] != heap[1][0]:
                num = heapq.heappop(heap)
                print(num[1])
            else:
                if heap[0][1] <= heap[1][1]:
                    num = heapq.heappop(heap)
                    print(num[1])
                else:
                    num = heap.pop[1]
                    print(num[1])
        elif heap == []:
            print(0)
        else:
            num = heapq.heappop(heap)
            print(num[1])
    else:
        heapq.heappush(heap,(abs(x), x))
