#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    # if N == 1 or N == 2:
    #     print(1)
    #     return
    sing = 0
    now = A[0]
    ans = 1
    for a in A[1:]:
        if sing == 0:
            if now < a:
                sing = 1
            elif now > a:
                sing = -1
        elif sing > 0:
            if not ( now <= a):
                ans += 1
                sing = 0
        else:
            if not ( now >= a ):
                ans += 1
                sing = 0
        now = a
    print(ans)
if __name__ == '__main__':
    main()
