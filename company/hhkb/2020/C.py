#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    P = list(map(int,input().split()))
    Judge = [True]*(2*10**5+2)
    ANS = []
    now = 0
    for p in P:
        Judge[p] = False
        for i in range(now, 2*10**5+2):
            if Judge[i]:
                now = i
                break
        ANS.append(now)
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
