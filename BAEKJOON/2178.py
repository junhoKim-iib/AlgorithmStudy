from collections import deque
N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input())))


mx = (0,0,1,-1)
my = (1,-1,0,0)

def bfs(x,y):
    
    path = deque()
    path.append((x,y))
    
    while path:
        x, y = path.popleft()

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                path.append((nx, ny))

    return maze[N-1][M-1]
        
print(bfs( 0, 0))