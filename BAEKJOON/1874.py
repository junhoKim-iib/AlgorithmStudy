import sys
n_input = sys.stdin.readline

n = int(n_input())
cur_n = 1
answer_list = []
stack = []
for _ in range(n):
    target = int(n_input())
    while cur_n <= target:
        stack.append(cur_n)
        answer_list.append("+")
        cur_n += 1
    if stack[-1] != target:
        print("NO")
        exit()
    else:
        stack.pop()
        answer_list.append("-")

print("\n".join(answer_list))