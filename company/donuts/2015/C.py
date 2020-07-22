#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    H = list( map( int, input().split()))
    stack = []
    ANS = [0]*N
    
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
