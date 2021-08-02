#import sys
#input = sys.stdin.readline
# from bisect import bisect_left
def main():
    K = int(input())
    ans = 0
    A = [i**2 for i in range(10**3)]
    for i in range(1, K+1):
        L = K//i
        for j in range(1,L+1):
            ans += L//j
    print(ans)
if __name__ == '__main__':
    main()
