
#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    # if N%K == 0:
    #     print(0)
    #     return
    print( min(N%K, K - N%K))
if __name__ == '__main__':
    main()
