#import sys
#input = sys.stdin.readline

from bisect import bisect_left
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    ANS = [0]*30
    for i in range(30):
        t = pow(2,i)
        D = sorted([ b%(t*2) for b in B])
        now = 0

        for a in A:
            a %= t*2
            now += (bisect_left(D,t*2-a) - bisect_left(D, t-a)) + (bisect_left(D, 4*t-a) - bisect_left(D, t*3-a))
#            print( bisect_left(D,t*2-a), bisect_left(D, t-a), bisect_left(D, 4*t-a), bisect_left(D, t*3-a))
        ANS[i] = now%2
#    print(ANS)
    ans = 0
    for i in range(30):
        ans += ANS[i]*pow(2,i)
    print(ans)
        
if __name__ == '__main__':
    main()
