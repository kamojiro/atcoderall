R, G, B, N = map( int, input().split())
ans = 0
for i in range(N//R+1):
    for j in range(N//G+1):
        if i*R + j*G <= N:
            if (N-R*i-j*G)%B == 0:
                ans += 1
        else:
            break
print(ans)
