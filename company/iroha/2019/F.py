N, K = map( int, input().split())
ans = []
now = 0
for i in range(2, int(N**(1/2))+1):
    if N%i == 0:
        while N%i == 0 and now < K-1:
            now += 1
            ans.append(i)
            N //= i
        if now == K-1:
            break
if now < K-1 or N == 1:
    print(-1)
else:
    ans.append(N)
    print( " ".join( map( str, ans)))

