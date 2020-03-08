import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations
def main():
    N = int( input())
    E = [[] for _ in range(N)]
    AB = [ tuple( map( lambda x:int(x)-1, input().split())) for _ in range(N-1)]
    T = [0]*N
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
        T[a] += 1
        T[b] += 1
    d = deque()
    P = [-1]*N
    F = [[] for _ in range(6)]
    for i in range(N):
        if T[i] == 1:
            P[i] = 0
            F[0].append(i)
            d.append(i)
            break

    while d:
        v = d.popleft()
        n = P[v]
        for w in E[v]:
            if P[w] == -1:
                d.append(w)
                P[w] = (n+1)%6
                F[(n+1)%6].append(w)

    L = [ len(F[i]) for i in range(6)]
    check = True
    pp = [0,0,0]
    qq = [0,1,2]
    for q in permutations( range(3)):
        for i in range(8):
            p = [i%2, i//2%2, i//4%2]
            check = True
            count = [N//3, (N+2)//3, (N+1)//3]
            for l in range(3):
                j = q[l]
                if p[j] == 0:
                    s = 1
                    t = 2
                else:
                    s = 2
                    t = 1
            
                if count[s] > L[j]:
                    count[s] -= L[j]
                else:
                    c = L[j] - count[s]
                    if count[0] < c:
                        check = False
                        break
                    count[0] -= c

                if count[t] > L[j+3]:
                    count[t] -= L[j+3]
                else:
                    c = L[j+3] - count[t]
                    if count[0] < c:
                        check = False
                        break
                    count[0] -= c
            if check:
                pp = p
                qq = q
                break
        if check:
            break

    count = [N//3, (N+2)//3, (N+1)//3]
    ds = [deque([ i*3+3 for i in range(count[0])]),  deque([ i*3+1 for i in range(count[1])]),  deque([ i*3+2 for i in range(count[2])])]
    ANS = [0]*N
    for j in range(3):
        i = qq[j]
        x = i
        y = i+3
        if pp[i] == 0:
            s = 1
            t = 2
        else:
            s = 2
            t = 1
        for w in F[x]:
            if ds[s]:
                #count[s] -= 1
                ANS[w] = ds[s].popleft()
            elif ds[0]:
                #count[0] -= 1
                ANS[w] = ds[0].popleft()
            else:
                #count[t] -= 1
                ANS[w] = ds[t].popleft()

        for w in F[y]:
            if ds[t]:
                #count[t] -= 1
                ANS[w] = ds[t].popleft()
            elif ds[0]:
                #count[0] -= 1
                ANS[w] = ds[0].popleft()
            else:
                #count[s] -= 1
                ANS[w] = ds[s].popleft()
               
    print( " ".join( map( str, ANS)))
    
    
if __name__ == '__main__':
    main()
