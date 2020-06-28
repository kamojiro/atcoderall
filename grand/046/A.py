#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        return a

def main():
    X = int( input())
    # if X > 90:
    #     X -= 90
    for i in range(1, X+1):
        if i*360%X == 0:
            print(i*360//X)
            return
if __name__ == '__main__':
    main()
