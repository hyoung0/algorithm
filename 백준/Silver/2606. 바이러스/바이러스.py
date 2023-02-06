def pprint(a):
    for i in a:
        print(i)
N = int(input())
t = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    

    print(visited.count(True) - 1)
dfs(1)