str_list = []
max_len = 0
for i in range(5):
    str_list.append(input())
    if len(str_list[i]) > max_len:
        max_len = len(str_list[i])

for i in range(max_len):
    for j in range(5):
        try:
            print(str_list[j][i], end='')

        except:
            continue
