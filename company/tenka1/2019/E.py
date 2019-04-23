def factors(z):
    ret = []
    for i in range(2, int(z**(1/2))+1):
        if z%i == 0:
            ret.append(i)
            while z%i == 0:
                z //= i
    if z != 1:
        ret.append(z)
    return ret
N = int( input())
A = [ int( input()) for _ in range(N+1)]
for i in range(N,-1,-1):
    if A[i] != 0:
        Primes = factors(abs(A[i]))
        break
ANS = []
for p in Primes:
    if p >= N+1:
        check = 1
        for i in range(N+1):
            if A[i]%p != 0:
                check = 0
                break
        if check == 1:
            ANS.append(p)
    else:
        poly = [0]*(p-1)
        for i in range(N+1):
            poly[(N-i)%(p-1)] = (poly[(N-i)%(p-1)] + A[i])%p
        check = 1
        if sum(poly) != 0:
            check = 0
        # if sum(poly[1:]) != 0 or poly[1] != 0:
        #     check = 0
        # if sum(poly) == 0:
        #     check = 1
    # if poly[0] != p-1 or poly[p-1] != 1:
    #     check = 0
    # for i in range(1, p-1):
    #     if poly[i] != 0:
    #         check = 0
    # if p == 2:
    #     if A[N]%2 == 0 and sum(A)%2 == 0:
    #         check = 1
    # if sum(poly) == 0:
    #     check = 1
        if check == 1:
            ANS.append(p)
for ans in ANS:
    print(ans)
