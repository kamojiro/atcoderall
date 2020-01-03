#import sys
#input = sys.stdin.readline
from itertools import product, combinations

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
    
    V = [0 for _ in range(3**9)]
    for q in product(range(1,3), repeat=9):
        V[ three_integer(q)] = get_point(q)
    P = [3**(8-i) for i in range(9)]
    for i in range(1,10):
        if i%2 == 1:
            cal = max
            unit = 0
        else:
            cal = min
            unit = 10000
        for c in combinations([0]*i+[1]*(9-i), 9): #1が埋まってるところ
            T = []
            for q in product( range(1,3), repeat=i):
                base = 0
                value = unit
                now = 0
                for j in range(9):
                    if c[j] == 1:
                        base += P[j]
                    else:
                        print(i, now, c, q)
                        T.append(q[now])
                        now += 1
                        #                print(c, q, three_adic(base))
                for r in product( range(1, 3), repeat=i):
                    branch = base
                    print(r, T)
                    for k in range(i):
                        branch += r[k]*P[T[k]]
                    print(c, base, three_adic(base), branch, 3**9-1)
                    value = cal(value, V[branch])
                V[base] = value
    print( V[0])
                    
        
if __name__ == '__main__':
    main()
