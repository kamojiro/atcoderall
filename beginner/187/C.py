#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int(input())
    S = [ input() for _ in range(N)]
    d = defaultdict(lambda : False)
    for s in S:
        d[s] = True
    for s in S:
        if s[0] != "!":
            if d["!"+s]:
                print(s)
                return
    print("satisfiable")
if __name__ == '__main__':
    main()
