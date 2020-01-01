#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    C = Counter( input())
    ANS = [ C[ chr( ord('A') + i)] for i in range(6)]
    print(" ".join( map( str, ANS)))
if __name__ == '__main__':
    main()
