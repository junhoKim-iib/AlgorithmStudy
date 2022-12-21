import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


trav = 0
queue_list = []

def bfs ( graph, R):
    global trav
    trav += 1
    visited[R] = trav
    print(R, end=' ')
    queue_list.append(R)
    while len(queue_list) > 0:
        node = queue_list.pop(0)
        for i in graph[node]:
            if visited[i] == 0:
                print(i, end=' ')
                trav += 1
                visited[i] = trav
                queue_list.append(i)



def dfs(graph, R):
    global trav
    trav += 1
    visited2[R] = trav
    print(R, end=' ')
    for i in graph[R]:
        if visited2[i] == 0:
            dfs(graph, i)


N, M, R = map(int, input().split())
visited = [0 for _ in range(N+1)]
visited2 = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for _, i in enumerate(range(N+1)):
    graph[i].sort()


dfs(graph, R)
trav = 0
print('')
bfs(graph, R)