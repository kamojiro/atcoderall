#import sys
#input = sys.stdin.readline
def main():
    N, X = map(int,input().split())
    VP = [tuple(map(int,input().split())) for _ in range(N)]
    X *= 100
    now = 0
    for i, vp in enumerate(VP):
        v, p = vp
        now += v*p
        if now > X:
            print(i+1)
            return
    print(-1)
if __name__ == '__main__':
    main()
    
