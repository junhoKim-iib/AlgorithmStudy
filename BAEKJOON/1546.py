n = int(input())
list1 = list(map(int,input().split()))

biggest = max(list1)

for i in range(n):
    list1[i] = list1[i]/biggest*100

print(sum(list1)/n)

