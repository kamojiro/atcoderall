#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    X = list( map( int, input().split()))
    now = 10000000
    for i in range(1,101):
        t = 0
        for x in X:
            t += (x-i)**2
        if t < now:
            now = t
    print(now)
if __name__ == '__main__':
    main()
