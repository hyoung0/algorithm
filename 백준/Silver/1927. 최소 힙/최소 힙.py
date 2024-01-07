import heapq
import sys
input = sys.stdin.readline

heap = []

T = int(input())
for t in range(T):
    x = int(input())
    if x == 0:
        if heap != []:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)