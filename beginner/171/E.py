#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    t = 0
    for a in A:
        t ^= a
    print( " ".join( map( str, [t^a for a in A])))
if __name__ == '__main__':
    main()
