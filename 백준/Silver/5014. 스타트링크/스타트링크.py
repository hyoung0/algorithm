from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs():
    queue = deque([S])
    visited = [0] * (F + 1)
    visited[S] = 1
    while queue:
        c = queue.popleft()
        if c == G:
            print(visited[G] - 1)
            return

        up = c + U
        down = c - D
        if up <= F and not visited[up]:
            queue.append(up)
            visited[up] = visited[c] + 1
        if down > 0 and not visited[down]:
            queue.append(down)
            visited[down] = visited[c] + 1
    else:
        print('use the stairs')
        return
bfs()