#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    p = int(input())
    d = defaultdict(int)
    Q = 998244353
    t = p-1
    for i in rngea(2, int(t**(1/2))+1):
        while t%i == 0:
            d[i] += 1
            t //= i
    if t > 0:
        d[t] += 1
    ans = 2 + (p-1)%Q*(p-2)%Q
    for key, value in d.items():
        x = 0
        x += 

    print(ans%Q)
    
    


if __name__ == '__main__':
    main()
