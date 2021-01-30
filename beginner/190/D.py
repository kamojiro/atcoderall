#import sys
#input = sys.stdin.readline
from collections import defaultdict

def factors(N): #約数を全て求める。ただし、順不同
    from collections import deque
    ret = deque()
    middle = int( N**(1/2))
    for i in range(1, middle):
        if N%i == 0:
            ret.append(i)
            ret.append(N//i)
            
    if N%middle == 0:
        ret.append(middle)
        if middle != N//middle:
            ret.append(N//middle)
    return ret

def main():
    N = int(input())
    ans = 0
    F = factors(N*2)
    d = defaultdict(lambda:True)
    N2 = N*2
    for a in F:
        b = N2//a
        s = a+b-1
        t = b-a+1
        # print(s,t)
        if s%2 == 0 and t%2 == 0:
            if s > t:
                s, t = t, s
            if d[(s,t)]:
                ans += 1
                d[(s,t)] = False
    print(ans)
if __name__ == '__main__':
    main()
