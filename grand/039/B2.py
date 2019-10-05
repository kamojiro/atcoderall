import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    S = [ list( map( int, list( input())[:-1])) for _ in range(N)]
    E = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                E[i].append(j)
    
    d = deque([0])
    V = [-1]*N
    V[0] = 1
    
    while d:
        v = d.pop()
        now = V[v]
        for w in E[v]:
            if V[w] == -1:
                V[w] = now+1
                d.append(w)
                continue

            if (now + V[w])%2 == 1:
                continue
            print(-1)
            return
    ans = 2

    for i in range(N):
        d = deque([i])
        V = [-1]*N
        V[i] = 1
        check = True
        while d:
            v = d.popleft()
            now = V[v]
            for w in E[v]:
                if V[w] == -1:
                    V[w] = now+1
                    d.append(w)
                    continue
                if now+1 == V[w] or now-1 == V[w]:
                    continue
                check = False
                break
            if not check:
                break
        if not check:
            continue
        if max(V) > ans:
            ans = max(V)
    print(ans)
    
            
                
if __name__ == '__main__':
    main()
