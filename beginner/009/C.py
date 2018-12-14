from collections import Counter, deque
N, K = map( int, input().split())
S = list( input())
SS = sorted(S)
DS = deque(S)
ans = ''
if N-1 <= K:
    for k in SS:
        ans += k*CS[k]
else:
    cnt = 0
    letters = 0
    while cnt <= K and letters != N:
        moji = DS.popleft()
        if moji == SS[letters]:
            letters += 1
            ans += moji
        elif cnt <= K:
            for i in range(K-letters,-1,-1):
                if SS[i] == moji:
                    SS[i] = moji
                    mojinum = i
                    break
            cnt += 1
            letters += 1
            ans += moji
        else:
            break
    if letters != N:
        for _ in range(N - letters):
            ans += DS.popleft()
print(ans)
    
    

