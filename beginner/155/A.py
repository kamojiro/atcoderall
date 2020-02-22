#import sys
#input = sys.stdin.readline
def main():
    A = list( map( int, input().split()))
    A.sort()
    if A[0] == A[1] and A[1] != A[2]:
        print("Yes")
        return
    if A[1] == A[2] and A[1] != A[0]:
        print("Yes")
        return
    print("No")
if __name__ == '__main__':
    main()
