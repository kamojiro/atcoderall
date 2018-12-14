from itertools import accumulate

N = int( input())
A = list( map( int, input().split()))
a, b = 0, 2
ans = 10**9 + 1
S = list(accumulate(A))
for i in range(1,N-2):
    while S[a] < S[i] - S[a+1]:
        a += 1
    b = max(b,i+1)
    while S[b] - S[i] < S[-1] - S[b+1]:
        b += 1
    ans = min( ans, max(S[a], S[i] - S[a], S[b] - S[i], S[-1] - S[b]) - min(S[a], S[i] - S[a], S[b] - S[i], S[-1] - S[b]))
print(ans)
