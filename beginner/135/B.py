#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    now = 0
    P = list( map( int, input().split()))
    for i in range(1, N+1):
        if i != P[i-1]:
            now += 1
    if now == 2 or now == 0:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()
