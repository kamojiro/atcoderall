#import sys
#input = sys.stdin.readline
def main():
    A, R, N = map( int, input().split())
    p = 10**9
    if R == 1:
        if A <= p:
            print(A)
        else:
            print("large")
        return
    now = A
    for _ in range(N-1):
        now *= R
        if now > p:
            print("large")
            return
    print(now)
if __name__ == '__main__':
    main()
