from collections import Counter, deque
N, K = map( int, input().split())
S = list( input())
SS = sorted(S)
DS = deque(S)
Ans = [ '?' for _ in range(N)]
red = []
for i in range(N):
    if S[i] == SS[i]:
        Ans[i] = SS[i]
    else:
        red.append(S[i])
Lr = len(red)
if Lr <= K:
    ans = ''.join(SS)
else:
    V = [ False for _ in range(Lr)]
    Sred = sorted(red)
    cnt = 0
    while cnt != K:
        
    ans = ''
    for i in range(N):
        if Ans[i] == '?':
            ans += newred.popleft()
        else:
            ans += Ans[i]
print(ans)
