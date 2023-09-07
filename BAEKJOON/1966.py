import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    doc_num, target = map(int, input().split())
    q_list = list(map(int, input().split()))

    cnt = 1

    max_val = max(q_list)
    list_len = len(q_list)  

    while not (q_list[target] == max_val and target == 0):

        if q_list[0] != max_val:
            q_list.append(q_list.pop(0))
            target = (target - 1) % list_len
        
        else:
            q_list.pop(0)
            cnt += 1
            list_len -= 1
            target = (target - 1) % list_len
            max_val = max(q_list)

    print(cnt)