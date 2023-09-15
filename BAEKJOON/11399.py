n = int(input())

person_list = list(map(int, input().split()))

person_list.sort()

answer = 0

for i in range(len(person_list)):
    answer += sum(person_list[0:i+1])


print(answer)