#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = int(input())
    print(S[N-1])
    print(S[N-3:N+3])
if __name__ == '__main__':
    main()
