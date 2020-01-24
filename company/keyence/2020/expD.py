#import sys
#input = sys.stdin.readline
from collections import deque, defaultdict
from itertools import permutations, product

def swap(x, i, j, b):
    i -= 1
    j -= 1
    ret = list(x)
    ret[i], ret[j] = ret[j], ret[i]
    if ret[i] > b:
        ret[i] -= b
    else:
        ret[i] += b
    if ret[j] > b:
        ret[j] -= b
    else:
        ret[j] += b
    return tuple(ret)

def main():
    N = 3
    q = deque([(1,2,3)])
    d = defaultdict( lambda : -1)
    d[q[0]] = 0
    b = 10
    while q:
        t = q.popleft()
        if d[swap(t,1,2,b)] == -1:
            d[swap(t,1,2,b)] = d[t]+1
            q.append( swap(t,1,2,b))
        if d[swap(t,2,3,b)] == -1:
            q.append( swap(t,2,3,b))
            d[swap(t,2,3,b)] = d[t]+1
        if d[swap(t,3,1,b)] == -1:
            d[swap(t,3,1,b)] = d[t]+1
            q.append( swap(t,3,1,b))
    for t in product(range(2), repeat=N-1):
        s = sum(t)%2
        for p in permutations( range(1,4)):
            q = list(p)
            for i in range(N-1):
                if t[i] == 1:
                    q[i] += b
            if s == 1:
                q[-1] += b
            print( tuple(q), d[tuple(q)])
        
    

if __name__ == '__main__':
    main()
