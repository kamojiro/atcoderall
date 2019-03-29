N = int( input())

if N == 3:
    print(2)
    print(1,3)
    print(2,3)
else:
    s = N%2
    N = N//2*2
    ans = 0
    for i in range(2,N//2+1):
        ans += 4*i - 4
    if s == 0:
        print(ans)
    else:
        print(ans+N)
    print(1, N-1)
    print(1,2)
    print(2,N)
    print(N-1,N)
    for i in range(2,N//2):
        for j in range(1,i+1):
            print(j, i+1)
            print(j, N-i)
            print(N+1-j, i+1)
            print(N+1-j, N-i)
    if s == 1 and N != 2:
        for i in range(1,N+1):
            print(i, N+1)
