from bisect import bisect_left, bisect_right
N = int( input())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
ans = 0
for k in range(29):
    T = 2**k
    S = 2**(k+1)
    kB = list( map( lambda x:x%S, B))
    kB.sort()
    check = 0
    for i in range(N):
        a = A[i]%S
        check += bisect_left(kB, (2*T-a))- bisect_left(kB, (T-a))
        check += bisect_left(kB, (4*T-a))- bisect_left(kB, (3*T-a))
        check %= 2
    if check == 1:
        ans += 2**k
print(ans)
