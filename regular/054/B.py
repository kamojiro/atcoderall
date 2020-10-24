#import sys
#input = sys.stdin.readline
def main():
    P = float( input())
    ans = P
    r = 91
    N = 10**6
    for i in range(1, 10**6):
        t = 91*i/N
        s = t + P/pow(2,t*2/3)
        if s < ans:
            ans = s
        else:
            break
    print(ans)
if __name__ == '__main__':
    main()
