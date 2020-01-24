#import sys
#input = sys.stdin.readline
def main():
    a, b = input().split()
    A = int(a*int(b))
    B = int(b*int(a))
    if A < B:
        print(B)
    else:
        print(A)
if __name__ == '__main__':
    main()
