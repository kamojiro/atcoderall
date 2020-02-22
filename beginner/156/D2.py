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
    n, a, b = map( int, input().split())
    print( (pow(2,n,Q) - cmb(n,a) - cmb(n,b)-1)%Q)
if __name__ == '__main__':
    main()
