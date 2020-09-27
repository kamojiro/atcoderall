#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    C = list(input())
    CC = Counter(C)
    ans = min(CC["R"], CC["W"])
    r = CC["R"]
    count = 0
    for c in C[:r]:
        if c == "W":
            count += 1
    ans = min(ans, count)
    print(ans)
if __name__ == '__main__':
    main()
