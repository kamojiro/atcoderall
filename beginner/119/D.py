from bisect import bisect_left
A, B, Q = map( int, input().split())
S = [ int( input()) for _ in range(A)]
T = [ int( input()) for _ in range(B)]
X = [ int( input()) for _ in range(Q)]
for i in range(Q):
    q = X[i]
    ANS = []
    # jinja kara
    JP = []
    s = bisect_left(S, q)
    if s == 0:
        JP.append(S[0])
    elif s == A:
        JP.append(S[A-1])
    else:
        JP.append(S[s])
        JP.append(S[s-1])
    while JP:
        f = JP.pop()
        z = abs(f-q)
        t = bisect_left(T, f)
        if t == 0:
            ANS.append( z + abs(f - T[0]))
        elif t == B:
            ANS.append( z + abs(f - T[B-1]))
        else:
            ANS.append( z + abs(f - T[t]))
            ANS.append( z + abs(f - T[t-1]))
    # tera kara
    TP = []
    t = bisect_left(T, q)
    if t == 0:
        TP.append(T[0])
    elif t == B:
        TP.append(T[B-1])
    else:
        TP.append(T[t])
        TP.append(T[t-1])
    while TP:
        f = TP.pop()
        z = abs(f-q)
        s = bisect_left(S, f)
        if s == 0:
            ANS.append( z + abs(f - S[0]))
        elif s == A:
            ANS.append( z + abs(f - S[A-1]))
        else:
            ANS.append( z + abs(f - S[s]))
            ANS.append( z + abs(f - S[s-1]))
    print( min(ANS))
    
    
