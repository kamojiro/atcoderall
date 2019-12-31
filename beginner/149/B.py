#import sys
#input = sys.stdin.readline
def main():
    A, B, K = map( int, input().split())
    if A >= K:
        print(A-K, B)
        return
    K -= A
    if B >= K:
        print(0, B-K)
        return
    print(0, 0)
if __name__ == '__main__':
    main()
