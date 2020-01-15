#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n == 1:
        return False
    for i in range(1, int(n**(1/2)) + 1):
        if n%i == 0:
            return False
    return True
    
def main():
    a, b = map( int, input().split())
    d = gcd(a,b)
    if d == 1:
        print(1)
        return
    if is_prime(d):
        print(2)
        return
    ans = 1
    for i in range(2, d+1):
        if d%i == 0:
            ans += 1
        while d%i == 0:
            d //= i
        if d == 1:
            break
    print(ans)

if __name__ == '__main__':
    main()
