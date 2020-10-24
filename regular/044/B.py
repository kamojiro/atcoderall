#import sys
#input = sys.stdin.readline
from collections import Counter
Q = 10**9+7
def main():
    N = int(input())
    A = list(map(int,input().split()))
    if A[0] > 0:
        print(0)
        return
    CA = Counter(A)
    if CA[0] > 1:
        print(0)
        return
    B = list(set(A))
    B.sort()
    for i, b in enumerate(B):
        if i != b:
            print(0)
            return
    now = 1
    ans = 1
    invtwo = pow(2,Q-2,Q)
    for c in B:
        b = CA[c]
        ans *= pow((pow(2,now,Q)-1),b,Q)
        # print(c, now, pow((pow(2,now,Q)-1),b,Q))
        ans %= Q
        # t = 1
        # p = 1
        # for i in range(0,b-1,2):
        #     # print(b,i,b-i,b-i-1, (b-i)*(b-i-1)*invtwo%Q)
        #     p *= (b-i)*(b-i-1)*invtwo%Q
        #     p %= Q
        #     t += p
        #     t %= Q
        # print(b,t)
        # ans *= t
        ans *= pow(2, b*(b-1)//2,Q)
        ans %= Q
        now = b
    print(ans)
if __name__ == '__main__':
    main()
