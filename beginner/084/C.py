N = int(input())
C = [0]*(N-1)
for i in range(N-1):
    C[i] = list( map( int, input().split()))
for i in range(N-1):
    k = i
    ans = 0
    while k < N-1:
        if ans <= C[k][1]:
            ans = C[k][1] + C[k][0]
        else:
            ans += (C[k][2] - ans)%C[k][2] + C[k][0]
        k += 1
    print(ans)
print(0)
