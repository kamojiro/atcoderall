#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    cnt = 0
    l = 0
    r = 10**9+1
        
    ans = 0
    while r-l > 1:
        m = (l+r)//2
        k = 0
        # print(l,r)
        for a in A:
            k += ((a+m-1)//m)-1
        if k <= K:
            r = m
        else:
            l = m
    print(r)
if __name__ == '__main__':
    main()
