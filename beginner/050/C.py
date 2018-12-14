from collections import Counter
N = int( input())
A = Counter(list( map( int, input().split())))
Q = 10**9 + 7
ans = 1
for i in range(N-1, 0, -2):
    if A[i] == 1:
        ans = 0
        break
if N%2 == 1:
    if A[0] != 1:
        ans = 0
print(ans*pow(2,N//2,Q))










