#import sys
#input = sys.stdin.readline
# from collections import Counter
def main():
    N = int( input())
    t = 10**18
    A = list( map( int, input().split()))
    ans = 1
    # if Counter(A)[0] > 0:
    #     print(0)
    #     return
    A.sort()
    for a in A:
        ans *= a
        if ans > t:
            print(-1)
            return
    print(ans)
if __name__ == '__main__':
    main()
