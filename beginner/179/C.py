#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ans = 0
    for i in range(1,N):
        ans += (N-1)//i
    print(ans)D.
if __name__ == '__main__':
    main()
