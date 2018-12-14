from collections import deque
K = int( input())
V = [0]*K
d = deque([(1,1)])
while 1:
    w, v = d.popleft()
    if v == 0:
        ans = w
        break
    if V[v] == 1:
        continue
    V[v] = 1
    if V[ (v+1)%K] == 0:
        # if (v+1)%K == 0: %こちらは必ずしも最小とは限らないため、%以下の方はWA
        #     ans = w+1
        #     break
        d.append((w+1 ,(v+1)%K))
    if V[ (v*10)%K] == 0:
        d.appendleft((w, (v*10)%K))
        # if (v*10)%K == 0:
        #     ans = w
        #     break
print(ans)
