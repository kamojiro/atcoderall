from collections import Counter, deque
N, K = map( int, input().split())
S = list( input())
SS = sorted(S)
V = [ True for _ in range(N)]
cnt = 0
letters = 0
while cnt < K and letters != N-1:
    moji = S[letters]
    letters += 1
    if moji == SS[letters]:
        pass
    else:
        if V[letters] == True:
            cnt += 1
            V[letters] = False
            for i in range(N-1,-1,-1):
                if S[i] == moji:
                    j = i
                    break
            if V[j] == True:
                cnt += 1
                if cnt > K:
                    pass
                else:
                    V[j] = False
                    S[letters], S[j] = S[j], S[letters]
            else:
                    S[letters], S[j] = S[j], S[letters]
        else:
            for i in range(N-1,-1,-1):
                if S[i] == moji:
                    j = i
                    break
            if V[j] == True:
                cnt += 1
                V[j] = False
                S[letters], S[j] = S[j], S[letters]
            else:
                S[letters], S[j] = S[j], S[letters]
                    
ans = ''.join(S)
print(ans)
