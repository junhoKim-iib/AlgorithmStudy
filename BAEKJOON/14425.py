
N, M = map(int, input().split())

S = set()

for _ in range(N):
    string = input().strip() 
    S.add(string)

count = 0
for _ in range(M):
    query = input().strip() 
    if query in S:
        count += 1

print(count)
