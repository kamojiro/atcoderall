#import sys
#input = sys.stdin.readline
def main():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    E = [[] for _ in range(N)]
    for x, y in [ tuple(map(lambda x: int(x)-1,input().split())) for _ in range(M)]:
        E[x].append(y)
    V = [10**10]*N
    ans = -10**10
    for i in range(N):
        if ans < A[i] - V[i]:
            ans = A[i] - V[i]
        now = min(A[i],V[i])
        for j in E[i]:
            if  now < V[j]:
                V[j] = now
    print(ans)
if __name__ == '__main__':
    main()
