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

def getFactorialInv(N):
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    ret = [1]*(N+1)
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
        ret[i] = ret[i-1]*inv[i]
    return ret

def getFactorial(N):
    ret = [1]*(N+1)
    for i in range(2,N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

def main():

    N, K = map( int, input().split())
    N = 10**5
    if K == 1:
        print(0)
        return
    A = list( map( int, input().split()))
    A.sort()
    ans = 0
#    cnt = 1
    fact = getFactorial(N)
    invfact = getFactorialInv(N)
    for i in range(K-1,N):
        # if i < N-1:
        #     if A[i+1] == A[i]:
        #         cnt += 1
        #         continue
        ans += fact[i]*invfact[K-1]%Q*invfact[i-(K-1)]%Q*A[i]%Q
#        print(A[i], fact[i]*invfact[K-1]%Q*invfact[i-(K-1)]%Q*cnt%Q)
        ans %= Q


    A = A[::-1]
    for i in range(K-1,N):
        # if i < N-1:
        #     if A[i+1] == A[i]:
        #         cnt += 1
        #         continue
        ans -= fact[i]*invfact[K-1]%Q*invfact[i-(K-1)]%Q*A[i]%Q
#        print(A[i], fact[i]*invfact[K-1]%Q*invfact[i-(K-1)]%Q*cnt%Q)
        ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()
