import sys
input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    d = dict()
    for i in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        d[(a,b)] = c
    V = [[1000000]*N for _ in range(N)]
    for i in range(N):
        V[i][i] = 0
    for (s,t), c in d.items():
        V[s][t] = V[t][s] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if V[i][k] + V[k][j] < V[i][j]:
                    V[i][j] = V[i][k] + V[k][j]
    ans = 0
    for (s,t), c in d.items():
        check = False
        for k in range(N**2):
            i = k//N
            j = k%N
            if V[i][s] + c + V[t][j] == V[i][j]:
                check = True
                break
        if check == False:
            ans += 1

    print(ans)
                
if __name__ == '__main__':
    main()
