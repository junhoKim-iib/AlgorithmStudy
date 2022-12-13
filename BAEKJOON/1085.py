x,y,w,h = input().split()

res = [int(x),int(y)]
res.append(abs(int(w) - int(x)))
res.append(abs(int(h) - int(y)))

print(min(res))