#import sys
#input = sys.stdin.readline
def main():
    A, B, C = map(int,input().split())
    Q = 998244353
    divtwo = pow(8,Q-2,Q)
    ans = A*(A+1)%Q*B%Q*(B+1)%Q*C%Q*(C+1)%Q*divtwo%Q
    print(ans)
if __name__ == '__main__':
    main()
