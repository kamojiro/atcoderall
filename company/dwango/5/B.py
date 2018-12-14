from itertools import accumulate
N, K = map( int, input().split())
A = list( map( int, input().split()))
accA = [0] + list( accumulate(A))
V = [1]*(N*(N+1)//2)
ans = 0
check = False
for i in range(40,-1,-1):
    W = [0]*(N*(N+1)//2)
    for l in range(N):
        for r in range(l+1,N+1):
            if V[l*(2*N+1-l)//2+r-l-1] == 0:#Vは現時点で採用されている部分列を示している
                #l*(2*N+1-l)//2+r-l-1はVの大きさに合わせて何番目を更新するか決定した。(時間節約のため)
                continue
            if (accA[r]-accA[l])%(2**(i+1)) >= 2**i:
                W[l*(2*N+1-l)//2+r-l-1] = 1
    if check == False:#初めに並ぶ 0 を無視するため
        if sum(W) >= K:
            check == True
        else:#無視して次のloopに遷移する
            continue
    if sum( V and W) >= K:#すでに確定している部分列と合わせて、K個以上あれば2**i桁目を採用する
        #V and W はlistの各成分のbool値の論理積を取っている
        ans += 2**i
        V = V and W
print(ans)

    


