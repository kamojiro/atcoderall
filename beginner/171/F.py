#import sys
#input = sys.stdin.readline
Q = 10**9+7
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

def main():
    K = int( input())
    S = input()
    N = len(S)
    ans = 0
    cmb = 1
    Inv = getInv(K+1)
    twenty_five = 1
    twenty_six = pow(26,K,Q)
    one_over_twenty_six = pow(26,Q-2,Q)
    for i in range(K+1):
        # ans += cmb*pow(25,i,Q)%Q*pow(26,K-i,Q)%Q
        # print(cmb, i, K-i)
        ans += cmb*twenty_five%Q*twenty_six%Q
        twenty_five *= 25
        twenty_five %= Q
        twenty_six *= one_over_twenty_six
        twenty_six %= Q
        ans %= Q
        cmb *= N+i
        cmb *= Inv[i+1]
        cmb %= Q
        
    print(ans)
if __name__ == '__main__':
    main()
