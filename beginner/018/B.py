#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = int( input())
    LR = [ tuple( map( int, input().split())) for _ in range(N)]
    for l, r in LR:
        S = S[:l-1] + S[l-1:r][::-1] + S[r:]
    print(S)
if __name__ == '__main__':
    main()
