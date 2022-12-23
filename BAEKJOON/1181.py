import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input().strip())

word_list = list(set(word_list))

word_list.sort()
word_list.sort(key=len)
for word in word_list:
    print(word)