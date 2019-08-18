#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    V = list( map( int, input().split()))
    V.sort()
    now = V[0]
    for i in range(1,N):
        now = (now+V[i])/2
    print(now)
if __name__ == '__main__':
    main()








