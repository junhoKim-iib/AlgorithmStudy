import sys
n, m = map(int, sys.stdin.readline().rstrip('\n').split())
HASH_SIZE = 797
res = []
class Hashing:
    def __init__(self, size):
        self.map = [[] for _ in range(797)]

    def mapping(self,key,value):
        self.map[int(''.join(map(str, [ord(ch) for ch in key]))) % HASH_SIZE].append({key:value})


    def search(self, key):
        hasing_key = int(''.join(map(str, [ord(ch) for ch in key]))) % HASH_SIZE
        hash_list = self.map[hasing_key]
        for dict in hash_list:
            if key in dict:
                return dict[key]

        



pw_list = Hashing(HASH_SIZE)

for i in range(n):

    key, value = sys.stdin.readline().rstrip('\n').split()
    pw_list.mapping(key, value)


for _ in range(m):
    pw = sys.stdin.readline().rstrip('\n')
    res.append(pw_list.search(pw))

for pw in res:
    print(pw)



