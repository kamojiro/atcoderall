#import sys
#input = sys.stdin.readline
def main():
    A, V = map( int, input().split())
    B, W = map( int, input().split())
    T = int( input())
    if A == B:
        print("YES")
        return
    if V <= W:
        print("NO")
        return
    d = V-W
    need = (abs(A-B)+d-1)//d
    if need <= T:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()
