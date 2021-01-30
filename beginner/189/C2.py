#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        t = A[i]
        for j in range(i,N):
            if A[j] < t:
                t = A[j]
            if ans < t*(j-i+1):
                ans = t*(j-i+1)
    print(ans)
if __name__ == '__main__':
    main()
