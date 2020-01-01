#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a = int( input())
    b = int( input())
    n = int( input())
    lcm = a*b//gcd(a,b)
    print((n+lcm-1)//lcm*lcm)
if __name__ == '__main__':
    main()
