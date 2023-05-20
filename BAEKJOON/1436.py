n = int(input())

movie_list = []

count = 1
num = 666
movie_list.append(num)

while count < n:
    num += 1 
    if '666' in str(num):
        count += 1
        movie_list.append(num)

print(movie_list[n-1])