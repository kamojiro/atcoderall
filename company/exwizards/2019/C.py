N, Q = map( int, input().split())
s = input()
TD = [list( input().split()) for _ in range(Q)]
l = -1
r = N
while r-l >= 2:
    m = (l+r)//2
    now = m
    fall = False
    for i in range(Q):
        t, d = TD[i]
        if d == "L":
            if s[now] == t:
                if now == 0:
                    fall = True
                    break
                now -= 1
        else:
            if s[now] == t:
                # if now = N-1:
                #     fall = True
                #     break
                if not now == N-1:
                    now += 1
    if fall == True:
        l = m
    else:
        r = m
L = l
l = max(L-2,-1)
r = N
while r-l >= 2:
    m = (l+r)//2
    now = m
    fall = False
    for i in range(Q):
        t, d = TD[i]
        if d == "L":
            if s[now] == t:
                if not now == 0:
                    now -= 1
        else:
            if s[now] == t:
                if now == N-1:
                    fall = True
                    break
                now += 1
    if fall == True:
        r = m
    else:
        l = m
R = r
print( max(0, R - L-1))
