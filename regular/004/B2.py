#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    Max = sum(D)
    print(Max)
    if N == 1:
        print(Max)
        return
    if N == 2:
        print(abs(D[0]-D[1]))
        return
    M = max(D)
    if M <= Max-M:
        print(0)
    else:
        print(2*M-Max)
        
if __name__ == '__main__':
    main()
