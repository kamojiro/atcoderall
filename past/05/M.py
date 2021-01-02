#import sys
#input = sys.stdin.readline
def main():
    N, L = map( int, input().split())
    A = list( map( int, input().split()))
    l = 1
    r = L+1
    while r-l > 0:
        m = (l+r)//2
        rest = 0
        check = True
        for a in A:
            if rest+a > L:
                if rest < m:
                    check = False
                    break
                rest = a
            if rest+a >= m:
                rest = 0
        if rest < m:
            if 
if __name__ == '__main__':
    main()
