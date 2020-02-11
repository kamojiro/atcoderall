#import sys
#input = sys.stdin.readline
def F(a,b,c):
    if a < b and a <c:
        return 3
    if a > b and a > c:
        return 1
    return 2
def main():
    a = int( input())
    b = int( input())
    c = int( input())
    print(F(a,b,c))
    print(F(b,a,c))
    print(F(c,a,b))
if __name__ == '__main__':
    main()
