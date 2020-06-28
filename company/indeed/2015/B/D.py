#import sys
#input = sys.stdin.readline
def main():
    N, C = map( int, input().split())
    A = list( map( int, input().split()))
    T = [[] for _ in range(C+1)]
    for i, a in enumerate(A):
        T[a].append(i)
    for i in range(C+1):
        T[i].append(N)
    base = N*(N+1)//2
    ANS = []
    # print(T)
    for t in T[1:]:
        now = -1
        ans = base
        for k in t:
            # if k == now+1:
            #     now = k
            #     continue
            # print(now, k, (k-now)*(k-now-1)//2)
            ans -= (k-now)*(k-now-1)//2
            now = k
        ANS.append(ans)
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
