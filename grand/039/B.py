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
    ans = -1
    # for k in range(2, N+1):
    #     check = True
    #     V = [-1]*N
    #     V[0] = 0
    #     d = deque([[0,0]])
    #     while d:
    #         v, before = d.pop()
    #         cnt = (V[v]+1)%k
    #         for w in E[v]:
    #             if w == before:
    #                 continue
    #             if V[w] == -1:
    #                 V[w] = cnt
    #                 d.append([w,v])
    #                 continue
    #             if (V[v] + cnt )%k == 0:
    #                 continue
    #             if V[w] != cnt:
    #                 print(d, v,before, 'w', w,cnt, V)
    #                 check = False
    #                 break
    #         if not check:
    #             break
    #     print(k, check, V)
    #     if check:
    #         ans = k

    print(ans)
            
                
if __name__ == '__main__':
    main()
