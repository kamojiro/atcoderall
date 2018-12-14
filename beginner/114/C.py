V = [0]*11
N = int( input())
L = len( str(N))
ans = 0
if l < 4:
    if N >= 753:
        ans = 6
    elif N >= 735:
        ans = 5
    elif N >= 573:
        ans = 4
    elif N >= 537:
        ans = 3
    elif N >= 375:
        ans = 2
    elif N >= 357:
        ans = 1
else:
    N = list( map( int, list( str(N))))
    for i in range(3, l):
        ans += 3**i - (2**i - 2)*3 - 3
    a = N[0]
    T = 0
    if N < int( "3"*L):
        pass
    else:
        c = 1
        for i in range(L):
            if N[i] <= 2:
                c *= 1
            elif N[i] <= 
