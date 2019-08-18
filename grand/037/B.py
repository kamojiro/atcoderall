#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N = int( input())
    S = input()
    CNT = [0]*3
    ans = 1
    for s in S:
        if s == "R":
            CNT[0] += 1
        elif s == "G":
            CNT[1] += 1
        elif s == "B":
            CNT[2] += 1
        if CNT[0] > 0 and CNT[1] > 0 and CNT[2] > 0:
            ans = ans*CNT[0]%Q*CNT[1]%Q*CNT[2]%Q*N%Q
            N -= 1
            CNT[0] -= 1
            CNT[1] -= 1
            CNT[2] -= 1
    print(ans)
if __name__ == '__main__':
    main()
