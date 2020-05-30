#import sys
#input = sys.stdin.readline
def main():
    H1, M1, H2, M2, K = map( int, input().split())
    one = H1*60+M1
    two = H2*60+M2
    print( max(0, two - one - K))
if __name__ == '__main__':
    main()








