import sys
n_input = sys.stdin.readline

T = int(n_input())
matrix = [[i for i in range(15)]]

for row in range(1,15):
    matrix.append([sum(matrix[row - 1][:i]) for i in range(1,16)])

for _ in range(T):
    
    k = int(n_input())
    n = int(n_input())

    print(matrix[k][n])


