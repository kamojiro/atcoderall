#import sys
#input = sys.stdin.readline
def main():
    A, B, C = map( int, input().split())
    K = int( input())
    for _ in range(K):
        if B <= A:
            B *= 2
            continue
        if C <= B:
            C *= 2
    if C > B and B > A:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
