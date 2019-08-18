#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    now = 1
    for a in A:
        now *= a
    ans = now
    q = 0
    for a in A:
        q += now//a
    print(ans/q)
if __name__ == '__main__':
    main()
