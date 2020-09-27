#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    D = [ tuple( map( int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()
