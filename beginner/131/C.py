def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)
A, B, C, D = map( int, input().split())
CD = C*D//gcd(C,D)
print(B-A+1 - (B//C - (A-1)//C) - (B//D-(A-1)//D) + (B//CD - (A-1)//CD))
