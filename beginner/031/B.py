import sys
input = sys.stdin.readline
def main():
    L, H = map( int, input().split())
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    ANS = []
    for a in A:
        if a < L:
            ANS.append(L - a)
        elif H < a:
            ANS.append(-1)
        else:
            ANS.append(0)
    for a in ANS:
        print(a)
if __name__ == '__main__':
    main()
