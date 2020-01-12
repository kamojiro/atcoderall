#import sys
#input = sys.stdin.readline
Q = 10**9+7
# def getInv(N):#Qはmod
#     inv = [0] * (N + 1)
#     inv[0] = 1
#     inv[1] = 1
#     for i in range(2, N + 1):
#         inv[i] = (-(Q // i) * inv[Q%i]) % Q
#     return inv

def main():

    N, K = map( int, input().split())
    if K == 1:
        print(0)
        return
    A = list( map( int, input().split()))
    A.sort()
    ans = 0

    cnt = 1
    for i in range(K-1,N):
        if i >= K:
            cnt *= i*pow(i-(K-1), Q-2, Q)%Q
            cnt %= Q
        ans += cnt*A[i]

        ans -= cnt*A[N-1-i]
        ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()
