N = int( input())
ans = 0
C = [""]*N
A = [0]*N
for i in range(N):
    C[i], a = input().split()
    A[i] = int(a)
for i in range(N):
    if C[i] == "+":
        ans += A[i]
for i in range(N):
    if C[i] == "*":
        if A[i] > 0:
            ans *= A[i]
print( ans)
