N, M = map(int, input().split())

# up, right, down, left
move = [(-1,0), (0,1), (1,0), (0,-1)] 
x, y, dir = map(int, input().split()) # x, y, direction

limit = 0 # 4방향 모두 갈 수 없을 때를 위한 변수
cnt = 0 # 방문한 칸 수
map_list = [] # map list
for _ in range(M):  # map list 생성
    map_list.append(list(map(int, input().split()))) 
    
map_list[x][y] = 1 # 현재 위치 방문 처리
cnt += 1 # 현재 위치 방문 처리

while True: 
    dir = (dir - 1) % 4 # 왼쪽으로 회전
    limit += 1 # 한번 회전할 때마다 limit 증가
    next_x, next_y = x + move[dir][0], y + move[dir][1] # 다음 위치
    
    if map_list[next_x][next_y] == 0: # 다음 위치가 육지일 때
        x, y = next_x, next_y # 다음 위치로 이동
        map_list[x][y] = 1 # 다음 위치 방문 처리
        cnt += 1 # 다음 위치 방문 처리
        limit = 0 # 다음 위치 방문 처리 후 limit 초기화

    else:
        if limit == 4: # 4방향 모두 갈 수 없을 때
            dir = (dir + 2) % 4 # 뒤로 
            next_x, next_y = x + move[dir][0], y + move[dir][1] # 뒤로 한 칸 이동
    
            if map_list[next_x][next_y] == 1: # 뒤로 한 칸 이동한 곳이 바다일 때
                break # 종료
            else:  # 뒤로 한 칸 이동한 곳이 육지일 때
                x, y = next_x, next_y # 뒤로 한 칸 이동


print(cnt) # 방문한 칸 수 출력

    