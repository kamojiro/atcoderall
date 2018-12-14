N = int( input())
T = list( map( int, input().split())) + [0]
V = list( map( int, input().split())) + [0]
now = 0
end = min( V[0], now + T[0])
ans = 0
for i in range(N):
    # print(i)
    t = T[i]
    v = V[i]
    end = min( v, now + t)
    plus = 0
    for j in range(i, N):
        end = min( end, V[j+1]+plus)
        plus += T[j+1]
    x, y = (end + t - now)/2, (end + t + now)/2
    # print(now, end,v,t,x,y)
    if y <= v:
        # print("T")
        # print((now+y)*x/2, (end+y)*(t-x)/2)
        ans += (now+y)*x/2 + (end+y)*(t-x)/2
        # print((now+y)*x/2 + (end+y)*(t-x)/2)
    else:
        # print("D")
        # print((v+now)*(v-now)/2, (v+end)*(v-end)/2, v*(end-2*v+t+now))
        ans += (v+now)*(v-now)/2 + (v+end)*(v-end)/2+v*(end-2*v+t+now)
        # print((v+now)*(v-now)/2 + (v+end)*(v-end)/2+v*(end-2*v+t+now))
    now = end
print(ans)
