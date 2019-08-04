#import sys
#input = sys.stdin.readline
def main():
    M, _, K = map( int, input().split())
    X = list( map( int, input().split()))
    L = [0]*M
    for x in X:
        L[x-1] += 1
    ans = 0
    for i in range(M):
        now = L[i]
        for k in range(1,K+1):
            if i - k >= 0:
                if L[i-k] > 0:
                    now += 1
                    continue
            if i + k <= M-1:
                if L[i+k] > 0:
                    now += 1
                    continue
        if now > ans:
            ans = now
    print( ans)
if __name__ == '__main__':
    main()

