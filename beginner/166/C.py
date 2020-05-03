import sys
input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    H = list( map( int, input().split()))
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map( lambda x: int(x)-1, input().split())
        E[a].append(b)
        E[b].append(a)
    ans = 0
    for i in range(N):
        h = H[i]
        ans += 1
        for e in E[i]:
            if h <= H[e]:
                ans -= 1
                break
    print(ans)
if __name__ == '__main__':
    main()








