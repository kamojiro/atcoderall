from collections import deque
N = int( input())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
ans = 0
kata = []
need = []
for i in range(N):
    if A[i] < B[i]:
        need.append(B[i] - A[i])
        ans += 1
    elif B[i] < A[i]:
        kata.append(A[i] - B[i])
need.sort()
kata.sort(key=None, reverse = True)
now = 0
for n in need:
    while n > now:
        if kata:
            now += kata.pop(0)
            ans += 1
        else:
            ans = -1
            break
    now -= n
    if ans == -1:
        break
print( ans)
