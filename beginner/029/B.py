#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    S = [ Counter( input()) for _ in range(12)]
    print( sum([1 for i in range(12) if S[i]['r'] > 0 ]))
if __name__ == '__main__':
    main()
