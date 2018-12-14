N = int( input())
T = list( map( int, input().split()))
M = int( input())
PX = [ list( map( int, input().split())) for _ in range(M)]
S = sum(T)
for i in range(M):
    p, x = PX[i]
    print(S - T[p-1] + x)
