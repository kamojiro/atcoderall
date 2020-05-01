#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    S = Counter(input())
    ans = "Yes"
    if S["N"] > 0 or S["S"] > 0:
        if S["N"] == 0 or S["S"] == 0:
            ans = "No"
    if S["W"] > 0 or S["E"] > 0:
        if S["W"] == 0 or S["E"] == 0:
            ans = "No"
    print(ans)
if __name__ == '__main__':
    main()








