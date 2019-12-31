#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)

def main():
    a, b = map( int ,input().split())
    g = gcd(a, b)
    print(a*b//g)
if __name__ == '__main__':
    main()








