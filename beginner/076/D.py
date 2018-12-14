from itertools import accumulate
N = int( input())
T = list( map( int, input().split())) + [0]
V = list( map( int, input().split())) + [0]
now = 0
ans = 0
for i in range(N):
    v, t = V[i], T[i]
    nextv = min(V[i+1], v+t)
    sumt = 0
    for j in range(i+1,N+1):
        nextv = min( nextv, V[j]+sumt)
        sumt += T[j]
    print(nextv)
    if now == v:
        ans += abs( nextv - now)*v + (nextv + v)*(t -  abs( nextv - now))/2
    elif v == nextv:
        ans += ( now + v)*( t - abs(now-v))/2 + ( t - abs( now-v))*v
    elif (now + nextv + t)/2 < v:
        print(now, nextv)
        x = ( nextv - now + t)/2
        y = t-x
        ans += (now*2+x)*x/2 + (nextv*2+y)*y/2
    else:
        print(i, t*v, (v - now)**2/2, (v-nextv)**2/2)
        ans += t*v - (v - now)**2/2 - (v-nextv)**2/2
    now = nextv
print(ans)
