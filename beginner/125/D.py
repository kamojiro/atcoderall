N = int( input())
A = list( map( int, input().split()))
S = [ -A[i] for i in range(N) if A[i] <= 0]
T = list( map( abs, A))
ans = sum(T)

if len(S)%2 != 0:
    ans -= min(T)*2
print(ans)

