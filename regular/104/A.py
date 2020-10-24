#import sys
#input = sys.stdin.readline
def main():
    A, B = map(int,input().split())
    print((A+B)//2, (A-B)//2)
if __name__ == '__main__':
    main()
