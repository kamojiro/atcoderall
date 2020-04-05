import sys
input = sys.stdin.readline
def main():
    N = int( input())
    R, B =[], []
    for _ in range(N):
        x, c = input().split()
        if c == "R":
            R.append( int(x))
        else:
            B.append( int(x))
    R.sort()
    B.sort()
    print( "\n".join( map( str, R+B)))
if __name__ == '__main__':
    main()
