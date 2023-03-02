# Title: 유기농 배추
# Link: https://www.acmicpc.net/problem/1012
# Language: Python 3

dx = [0,0,1,-1] # 상하좌우
dy = [1,-1,0,0] # 상하좌우
cnt = 0 # 배추흰지렁이 수
def dfs(x, y): # dfs로 배추흰지렁이 수 세기
    stack = [(x,y)] #  스택에 좌표 넣기

    while stack: # 스택이 빌때까지
        x, y = stack.pop() # 스택에서 좌표 빼기
        maps[x][y] = 0 # 배추흰지렁이가 지나간 곳은 0으로 바꾸기
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i] # 상하좌우 좌표
            ny = y + dy[i] # 상하좌우 좌표
            # 좌표가 범위를 벗어나면 continue
            if nx < 0 or nx >= N or ny < 0 or ny>=M: 
                continue
             # 배추가 있으면 스택에 좌표 넣기       
            if maps[nx][ny] == 1:
                stack.append((nx,ny)) 


T = int(input()) # 테스트 케이스

for _ in range(T): # 테스트 케이스만큼 반복
    N, M, K = map(int, input().split()) # 가로, 세로, 배추 개수
    maps = [[0]* M for _ in range(N)] # 배추밭

    for _ in range(K): # 배추 개수만큼 반복
        x, y = map(int, input().split()) # 배추 좌표
        maps[x][y] = 1 # 배추가 있는 곳은 1로 바꾸기
    # 배추밭 탐색
    for i in range(N): 
        for j in range(M):
            if maps[i][j] == 1: # 배추가 있으면
                dfs(i,j) # dfs로 탐색
                cnt += 1 # 배추흰지렁이 수 증가
    
    print(cnt) # 배추흰지렁이 수 출력
    cnt = 0 # 배추흰지렁이 수 초기화

