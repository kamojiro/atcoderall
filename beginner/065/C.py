Q = 10**9 + 7
'''
#これは深すぎるらしい
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))%Q
'''
N, M = map( int, input().split())
N, M = min(N, M), max(N, M)
if N == M or N+1 == M:
    NN = 1
    MM = 1
    for i in range(1,N+1):
        NN = (NN*i)%Q
    if N == M:
        ans = (2*NN*NN)%Q
    elif N+1 == M:
        ans = (NN*NN*M)%Q
else:
    ans = 0
print(ans)

