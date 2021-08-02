#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    S = input()
    ans = 0
    now = ""
    d = defaultdict(int)
    before = ""
    for i, s in enumerate(S[::-1]):
        d[s] += 1
        if before != s:
            before = s
            continue
        # print(before, s)
        ans += i + 1 - d[s]
        d = defaultdict(int)
        d[s] = i+1
        before = s
    print(ans)
if __name__ == '__main__':
    main()
