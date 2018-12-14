from itertools import accumulate
N, X = map( int, input().split())
G = list( map( int, input().split()))
ans = 0
enG = list(accumulate(G))
enG.insert(0,0)
now = G[0]*5
for i in range(1,N):
    nowb, now =now, now+ 5*G[i] + 2*enG[i-1]
    if now <= nowb + G[i]*5 + X:
        pass
    else:
#        print('huga')
        ans += nowb + X
        now = G[i]*5
        enG = list(map(lambda x: x - enG[i], enG))
#        print(enG)
#    print(now)
#    print(ans)
ans += now + X
ans += N*X
print(ans)
    
        
    
