#import sys
#input = sys.stdin.readline
def main():
    S = list( input())
    N = int( input())
    S.sort()
    N -= 1
    ans = S[N//5] + S[N%5]
    print(ans)
if __name__ == '__main__':
    main()
