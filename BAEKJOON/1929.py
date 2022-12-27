n, m = map(int, input().split())

aristo = [ i for i in range(m+1) ]

for i in range(2, m):
    j = i * i
    while j <= m:
       aristo[j] = 0
       j += i

# drop 0 in the aristo[n:m] list
aristo = [ i for i in aristo[n:m+1] if i != 0 ]

for i in aristo:
    if i == 0 or i == 1:
        continue
    print(i)
    
