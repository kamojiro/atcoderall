#import sys
#input = sys.stdin.readline
def main():
    a, b = input().split()
    a = int(a)
    c, d = b.split(".")
    b = int(c)*100+int(d)
    print( a*b//100)
if __name__ == '__main__':
    main()
