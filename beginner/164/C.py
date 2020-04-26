#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    S = Counter( [ input() for _ in range(N)])
    print( len(S))
if __name__ == '__main__':
    main()








