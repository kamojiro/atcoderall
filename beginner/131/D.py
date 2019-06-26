#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    T = [ (0,0)]*N
    for i in range(N):
        a, b = map( int, input().split())
        T[i] = (b,a)
    T.sort()
    time = 0
    ans = "Yes"
    for i in range(N):
        time += T[i][1]
        if time > T[i][0]:
            ans = "No"
            break
    print(ans)
if __name__ == '__main__':
    main()
