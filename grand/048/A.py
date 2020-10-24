#import sys
#input = sys.stdin.readline
def solve():
    S = list(input())
    A = list("atcoder")
    T = sorted(S, reverse=True)
    print(T)
    print(A >= T)
    if A >= T:
        return(-1)
def main():
    T = int( input())
    ANS = [ solve() for _ in range(T)]
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
