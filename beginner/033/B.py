#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    Sum = 0
    P = []
    S = []
    for _ in range(N):
        s, p = input().split()
        p = int(p)
        Sum += p
        S.append(s)
        P.append(p)
    for i in range(N):
        if P[i]*2 > Sum:
            print(S[i])
            return
    print("atcoder")
if __name__ == '__main__':
    main()

