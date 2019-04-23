N = int( input())
S = input()
C = [0]*(N+1)
for i in range(N):
    if S[i] == ".":
        C[i+1] = C[i]
    else:
        C[i+1] = C[i] + 1
b = C[N]
w = N - b
ans = w
for i in range(N):
    if C[i+1] + N - i - 1 -b + C[i+1] < ans:
        ans = C[i+1] + N - i - 1 -b + C[i+1]
print(ans)
 





