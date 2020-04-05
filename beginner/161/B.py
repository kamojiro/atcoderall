#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    T = sum(A)
    count = 0
    for a in A:
        if a*4*M >= T:
            count += 1
    if count >= M:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
