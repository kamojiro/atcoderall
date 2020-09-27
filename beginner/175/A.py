#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    S = input()
    C = Counter(S)
    if C["R"] == 3:
        print(3)
    elif C["R"] == 2:
        if S[1] == "S":
            print(1)
        else:
            print(2)
    elif C["R"] == 1:
        print(1)
    else:
        print(0)
        
if __name__ == '__main__':
    main()
