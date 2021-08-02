#import sys
#input = sys.stdin.readline
def solve():
    L, R = map(int,input().split())
    if L == 0:
        return (R+1)*(R+2)//2
    elif R < L*2:
        return 0
    else:
        return (R-L*2+1)*(R-L*2+2)//2


def main():
    T = int( input())
    ANS = [ solve() for _ in range(T)]
    print("\n".join(map(str, ANS)))
if __name__ == '__main__':
    main()
