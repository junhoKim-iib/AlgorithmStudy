N = int(input())

def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
        

def LCM(mul, GCD_n):
    return mul // GCD_n




for _ in range(N):
    a, b = map(int,input().split())
    if a < b:
        a, b = b, a 
    gcd_n = GCD(a,b)
    
    print(LCM(a*b,gcd_n))