from collections import deque


N, M = map(int, input().split())
cnt = 0 # 판자 개수 카운트
type_1  = [(0,1), (0,-1)] # 가로로 이동할 수 있는 방향
type_2  = [(1,0), (-1,0)] # 세로로 이동할 수 있는 방향
maps = [] # 맵

# 맵 입력받기
for _ in range(N):
    maps.append(list(map(str, input())))

# bfs 탐색
def bfs(x, y):
    global cnt
    queue = deque() 
    queue.append((x,y))

    if maps[x][y] == '-': # 가로
        while queue: # 큐가 빌때까지
            x, y = queue.popleft() 
            for move in type_1: # 가로로 이동할 수 있는 방향
                nx = x + move[0] # 다음 x좌표
                ny = y + move[1] # 다음 y좌표

                # 범위를 벗어나면
                if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                    continue
                # 다음 좌표가 세로면
                if maps[nx][ny] == '|':
                    continue

                # 다음 좌표가 가로면
                if maps[nx][ny] == '-': 
                    maps[nx][ny] = 'x' # 방문처리
                    queue.append((nx,ny)) # 큐에 추가
        cnt += 1 # 최대 크기의 판자를 찾았으므로 카운트 증가
        
    elif maps[x][y] == '|': # 세로
        while queue:
            x, y = queue.popleft()
            for move in type_2: # 세로로 이동할 수 있는 방향
                nx = x + move[0]
                ny = y + move[1]
                # 범위를 벗어나면
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                # 다음 좌표가 가로면
                if maps[nx][ny] == '-':
                    continue
                # 다음 좌표가 세로면
                if maps[nx][ny] == '|':
                    maps[nx][ny] = 'x' # 방문처리
                    queue.append((nx,ny)) # 큐에 추가
        cnt += 1 # 최대 크기의 판자를 찾았으므로 카운트 증가

# 맵을 돌면서
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'x': # 방문했으면
            continue
        bfs(i,j) # bfs 탐색

    
print(cnt) # 카운트 출력