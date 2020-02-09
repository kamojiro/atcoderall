#import sys
#input = sys.stdin.readline
def main():
    H, N = map( int, input().split())
    A = list( map( int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
