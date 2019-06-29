#import sys
#input = sys.stdin.readline
def main():
    n = int( input())
    P = list( map( int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if P[i-1] < P[i] and P[i] < P[i+1]:
            ans += 1
        elif P[i-1] > P[i] and P[i] > P[i+1]:
            ans += 1
    print(ans)
        
if __name__ == '__main__':
    main()
