#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    N, K = map( int, input().split())
    ANS = [0]*(K+1)
    for x in range(K,0,-1):
        ans = pow(K//x,N,Q)
        for i in range(2, K+1):
            if x*i > K:
                break
            ans -= ANS[x*i]
        ANS[x] = ans%Q
    print( sum( [ANS[i]*i%Q for i in range(K+1)])%Q)
        
if __name__ == '__main__':
    main()
