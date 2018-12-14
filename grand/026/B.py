def gcd(a, b):
    while b:
        a, b = b, a % b
    return(a)

T = int(input())
for i in range(T):
    A,B,C,D = map(int,input().split())
    if B > D:
        print('No')
    elif A < B:
        print('No')
    elif C + 1 >= B:
        print('Yes')
    else:
        q = gcd(B,D)
        r = (A-C)%q
        if r == 0:
            r = q
        if C + r >= B:
            print('Yes')
        else:
            print('No')
        
