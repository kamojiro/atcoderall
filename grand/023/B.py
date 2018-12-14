N = int( input())
S = [ input() for _ in range(N)]
ans = 0
for k in range(N):
    check = True
    for i in range(N):
        for j in range(i+1,N):
            if not S[i][(j+k)%N] == S[j][(i+k)%N]:
                check = False
                break
        if not check:
            break
    if check:
        ans += N
print(ans)
