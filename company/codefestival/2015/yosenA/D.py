import sys
input = sys.stdin.readline
def main():
    N, M = map(int,input().split())
    X = [int(input()) for _ in range(M)]
    l = -1
    r = 2*10**9
    while r-l > 1:
        m = (l+r)//2
        now = 0
        for x in X:
            if now+1 < x-m:
                break
            if now < x:
                now = max(x, x+m-(x-now-1)*2, x+(m-(x-now-1))//2)
            else:
                now = x+m
        if now >= N:
            r = m
        else:
            l = m
    print(r)
        
if __name__ == '__main__':
    main()
