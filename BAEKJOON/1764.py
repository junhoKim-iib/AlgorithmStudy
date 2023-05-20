n, m = map(int, input().split())
HASH_SIZE = 797 # prime number for hashing
res = [] # list for result

# Hashing class
class Hashing: 
    # constructor
    def __init__(self, size):
        self.map = [[] for _ in range(797)] # list for hashing

    # mapping method
    def mapping(self, key):
        # input is string, so convert to ascii code and join them
        self.map[int(''.join(map(str, [ord(ch) for ch in key]))) % HASH_SIZE].append(key) # append key to hash list

    # search method
    def search(self, key):
        # input is string, so convert to ascii code and join them
        # and search key in hash list
        hash_list = self.map[int(''.join(map(str, [ord(ch) for ch in key]))) % HASH_SIZE]

        # if key in hash list, append key to result list
        if key in hash_list:
            res.append(key)

# create Hashing object
name_list = Hashing(HASH_SIZE)

# input name and mapping
for _ in range(n):
    name_list.mapping(input())

# search name and append to result list
for _ in range(m):
    name = input()
    name_list.search(name)


# print result
print(len(res))
res.sort() # sort result list
for name in res:
    print(name)