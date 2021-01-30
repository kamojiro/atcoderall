#import sys
#input = sys.stdin.readline
def main():
    A, B = input().split()
    SA = map( int, list(A))
    SB = map(int, list(B))
    
    print(max(sum(SA), sum(SB)))
if __name__ == '__main__':
    main()
