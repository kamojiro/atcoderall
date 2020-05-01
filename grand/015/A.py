#import sys
#input = sys.stdin.readline
def main():
    N, A, B = map( int, input().split())
    if A > B:
        print(0)
        return
    if N == 1 and A != B:
        print(0)
        return
    print( (A+B*(N-1)) - (A*(N-1)+B) + 1)
if __name__ == '__main__':
    main()
