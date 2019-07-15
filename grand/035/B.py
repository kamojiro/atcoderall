import sys
from collections import deque
input = sys.stdin.readline
def main():
    N, M = map( int ,input().split())
    ANS = []
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map( int, input().split())
        a, b = a-1, b-1
        E[a].append(b)
        E[b].append(a)
    W = [ len(E[i]) for i in range(N)]
    V = [0]*N
    for i in range(N):
        if V[i] != 0 or W[i] > 1:
            continue
        V[i] = -2
        a = E[i][0]
        ANS.append([a+1, i+1])
        V[a] = -1
        t = 1
        while W[a] <= 2:
            t = (t+1)%2
            if W[a] == 1:
                if t == 0:
                    print(-1)
                    return
                else:
                    break
            for b in E[a]:
                if V[b] == 0:
                    if t == 0:
                        ANS.append([a+1, b+1])
                    else:
                        ANS.append([b+1, a+1])
                    print(a,b,t-2)
                    V[b] = t-2
                    a = b
                    break
            else:
                break
        if W[a] > 2:
            V[a] = t
    now = -1
    for i in range(N):
        if V[i] == 0:
            now = i
            break
    if now == -1:
        for ans in ANS:
            print( " ".join( map( str, ans)))
        return
    d = deque([now])
    
            
            
if __name__ == '__main__':
    main()
