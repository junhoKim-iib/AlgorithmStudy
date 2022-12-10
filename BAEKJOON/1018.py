n,m = map(int,input().split())

matrix = []

for _ in range(n):
    matrix.append(input())


count = 0

idx_W = 0
idx_B = 0
res_list = []

for row in range(n-7):
   for col in range(m-7):
        idx_W = 0
        idx_B = 0
        for i in range(row, row+8):
            for j in range(col, col+8):

                if (i+j) %2 == 0:
                    if matrix[i][j] != 'W':
                        idx_W += 1
                    if matrix[i][j] !='B':
                        idx_B += 1

                else:
                    if matrix[i][j] != 'B':
                        idx_W += 1
                    if matrix[i][j] !='W':
                        idx_B += 1

        res_list.append(min(idx_B,idx_W))


print(min(res_list))
