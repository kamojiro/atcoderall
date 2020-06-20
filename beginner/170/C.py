#import sys
#input = sys.stdin.readline
def main():
    X, N = map( int, input().split())
    if N == 0:
        print(X)
        return
    Q = list( map( int, input().split()))
    # P.sort()
    Z = [True]*102
    for q in Q:
        Z[q] = False
    P = []
    for i in range(102):
        if Z[i]:
            P.append(i)
    # print(P)
    now = P[0]
    ab = abs(X-P[0])
    for p in P:
        pab = abs(X-p)
        if pab == ab:
            if p < now:
                now = p
        elif pab < ab:
            now = p
            ab = pab
    print(now)
if __name__ == '__main__':
    main()
