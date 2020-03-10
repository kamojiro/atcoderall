#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    a, b = map( int, input().split())
    K = int( input())
    P = list( map( int, input().split()))
    T = [0]*101
    T[a] += 1
    T[b] += 1
    for p in P:
        if T[p] > 0:
            print("NO")
            return
        T[p] += 1
    print("YES")
if __name__ == '__main__':
    main()
