from collections import deque
n = int(input())
A = list( map( int, input().split()))
B = deque()
reverse = 0
for i in range(n):
    if reverse == 0:
        B.append(A[i])
        reverse = 1
    else:
        B.appendleft(A[i])
        reverse = 0
B = list(B)
if reverse == 1:
    B = B[::-1]
print( ' '.join( list( map(str, B))))
