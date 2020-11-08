#import sys
#input = sys.stdin.readline
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 2
    gcd_deg = 0
    for k in range(2,1001):
        deg = 0
        for a in A:
            if a%k == 0:
                deg += 1
        if deg > gcd_deg:
            gcd_deg = deg
            ans = k
    print(ans)
if __name__ == '__main__':
    main()
