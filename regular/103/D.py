N = int( input())
P = [ list( map( int, input().split())) for _ in range(N)]
judge = 0
V = [0]*N
for i in range(N):
    a, b = P[i]
    judge += (a+b)%2
    V[i] = abs(a)+abs(b)
if judge == N or judge == 0:
    M = max(V)
    if M > 41:
        print(-1)
        N = 0
    else:
        print(M)
        arm = '1'
        for i in range(M-1):
            arm += ' 1'
        print(arm)

    for i in range(N):
        ans = ''
        x, y = P[i]
        a, b = 0, 0
        for _ in range(M):
            if a < x:
                ans += 'R'
                a += 1
            elif a > x:
                ans += 'L'
                a -= 1
            elif b <= y:
                ans += 'U'
                b += 1
            else:
                ans += 'D'
                b -= 1
        print(ans)
else:
    print(-1)
    
    
