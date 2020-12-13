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
    N, M = map( int, input().split())
    A = list(map(int,input().split()))
    n = N + M
    r = N + sum(A)
    if sum(A) > M:
        print(0)
        return
        
    print(cmb(n,r))
if __name__ == '__main__':
    main()
