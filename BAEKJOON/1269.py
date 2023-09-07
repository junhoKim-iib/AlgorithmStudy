import sys
n_input = sys.stdin.readline

A_num, B_num = map(int, n_input().split())

A_set = set(map(int, n_input().split()))
B_set = set(map(int, n_input().split()))

print(len(A_set - B_set) + len(B_set - A_set))