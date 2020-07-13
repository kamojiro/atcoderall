#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    S = [ input() for _ in range(N)]
    C = Counter(S)
    print("AC", "x", C["AC"])
    print("WA", "x", C["WA"])
    print("TLE", "x", C["TLE"])
    print("RE", "x", C["RE"])

if __name__ == '__main__':
    main()
