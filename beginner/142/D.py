#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def prime_factors(N): #約数を全て求める。ただし、順不同
    ret = 1
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            ret += 1
            while tmp%i == 0:
                tmp //= i
    if tmp != 1:
        ret += 1
    return ret

    
def main():
    a, b = map( int, input().split())
    d = gcd(a,b)
#    print(2, is_prime(2))
    if d == 1:
        print(1)
        return

    print(factors(d))

if __name__ == '__main__':
    main()
