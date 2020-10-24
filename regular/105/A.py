#import sys
#input = sys.stdin.readline
from itertools import product

def main():
    X = list(map(int,input().split()))
    s = sum(X)
    for P in product(range(2),repeat=4):
        now = 0
        for i in range(4):
            if P[i] == 1:
                now += X[i]
        if now == 0:
            continue
        if now == s - now:
            print("Yes")
            return
    print("No")
if __name__ == '__main__':
    main()
