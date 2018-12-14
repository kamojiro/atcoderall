N = int( input())
D = []
for i in range(N):
    D.append(int(input()))
D = sorted(D)
ans = 1
d_now = D[0]
for i in range(1,N):
    if d_now < D[i]:
        ans += 1
        d_now = D[i]
print(ans)
