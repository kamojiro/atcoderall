#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N = int( input())
    S = input()
    ans = 1
    R, G, B = 0, 0, 0
    for s in S:
        if s == "R":
            if G == 0 or B == 0:
                R += 1
                continue
            ans *= G*B%Q
            G -= 1
            B -= 1
            ans %= Q
        if s == "G":
            if R == 0 or B == 0:
                G += 1
                continue
            ans *= R*B%Q
            R -= 1
            B -= 1
            ans %= Q
        if s == "B":
            if R == 0 or G == 0:
                B += 1
                continue
            ans *= R*G%Q
            R -= 1
            G -= 1
            ans %= Q
    for i in range(1, N+1):
        ans *= i
        ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()
