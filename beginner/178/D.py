#import sys
#input = sys.stdin.readline
Q = 10**9+7
def cmb(n,r):
    if n-r < r: r = n-r
    if r == 0: return 1
    denominator = 1                       #分母
    numerator = 1                         #分子
    for i in range(r):
        numerator *= n-i
        numerator %= Q
        denominator *= i+1
        denominator %= Q
    return numerator*pow(denominator, Q-2, Q)%Q

def main():
    S = int( input())
    ans = 0
    for i in range(1, S//3+1):
        t = S - i*3
        ans += cmb(t+i-1,i-1)
        ans %= Q
    print(ans)
        
if __name__ == '__main__':
    main()
