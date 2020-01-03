from itertools import product, combinations
from collections import deque
def three_adic(x):
    ret = [0]*9
    for i in range(9):
        ret[8-i] = x%3
        x //= 3
    return ret

def three_integer(x):
    ret = 0
    for t in x:
        ret *= 3
        ret += t
    return ret


def main():
    B = [ list( map( int, input().split())) for _ in range(2)]
    C = [ list( map( int, input().split())) for _ in range(3)]
    def get_point(x):
        ret = 0
        for i in range(6):
            if x[i] == x[i+3]:
                ret += B[i//3][i%3]
        for i in range(3):
            for j in range(2):
                if x[i*3+j] == x[i*3+j+1]:
                    ret += C[i][j]
        return ret
    E = [set() for _ in range(3**9)]
    q = deque([0])
    B = [[] for _ in range(10)]
    P = [ 3**(8-i) for i in range(9)]
    W = [False]*(3**9)
    W[0] = True
    while q:
        v = q.popleft()
        V = three_adic(v)
        for i in range(9):
            if V[i] == 0:
                if not W[v+P[i]]:
                    E[v].add(v+P[i])
                    q.append(v+P[i])
                    W[v+P[i]] = True
                if not V[v+2*P[i]]:
                    E[v].add(v+2*P[i])
                    q.append(v+2*P[i])
                    W[v+2*P[i]] = True
        B[ sum([1 for v in V if v == 0])].append(v)
    V = [0]*(3**9)
    for q in product(range(1,3), repeat=9):
        V[ three_integer(q)] = get_point(q)
    for i in range(1,10):
        if i%2 == 1:
            calc = max
            unit = 0
        else:
            calc = min
            unit = 100000
        for v in B[i]:
            value = unit
            for w in E[v]:
                value = calc(value, V[w])
            V[v] = value
    print(B[9])
    print(V[0])
    
        
        
if __name__ == '__main__':
    main()
