N, Q = map( int, input().split())
S = input()
AAT = [0]*(N+1)
ATT = [0]*(N+1)
now = 0
ac = 0
for i in range(N):
    if S[i] == 'A':
        now = 1
    elif S[i] == 'C':
        if now == 1:
            ac += 1
        now = 0
    else:
        now = 0
    ATT[i] = ac
    if i == 0:
        continue
    AAT[i-1] = ac
AAT[N-1] = ac
for _ in range(Q):
    l, r = map( int, input().split())
    if l == 1:
        print(ATT[r-1])
    else:
        print( ATT[r-1] - AAT[l-2])
