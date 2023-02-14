N, K = map(int, input().split())

res = 0

while N >= K:
    div_max = (N // K) * K # N이 K로 나누어 떨어지지 않을 때, 가장 가까운 K의 배수
    res += (N-div_max) # N이 K로 나누어 떨어지지 않을 때, 1을 빼는 횟수

    N = div_max 
    res += 1 # N이 K로 나누어 떨어질 때, K로 나누는 횟수
    N //= K 

res += (N-1) # N이 K보다 작을 때, 1을 빼는 횟수
print(res)

