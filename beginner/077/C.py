import bisect as bisect
N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())
A = sorted(A)
B = sorted(B)
C = sorted(C)
ans = 0
for b in B:
    ans += bisect.bisect_left(A,b) * (N - bisect.bisect_right(C,b))
print(ans)
    








