N, K = map( int, input().split())
A = list( map( int, input().split()))
# 1の個数をそれぞれの桁でカウントしたい
V = [0]*41
for a in A:
    for i in range(40,-1,-1):
        if a%2 == 0:
            pass
        else:
            V[i] += 1
        a //= 2
        if a == 0:
            break
W = [0]*41
for i in range(40,-1,-1):
    if K%2 == 0:
        pass
    else:
        W[i] += 1
    K //= 2
    if K == 0:
        break
ans = 0
check = 0
for i in range(41):
    if W[i] == 1:
        if V[i] > N - V[i]:
            ans += (2**(40-i))*V[i]
            check = 1
        else:
            ans += (2**(40-i))*(N-V[i])
    else:
        if check == 0:
            ans += (2**(40-i))*V[i]
        else:
            if V[i] > N - V[i]:
                ans += (2**(40-i))*V[i]
            else:
                ans += (2**(40-i))*(N-V[i])
print( ans)
