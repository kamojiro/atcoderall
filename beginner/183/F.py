import sys
input = sys.stdin.readline
def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

from collections import defaultdict
def main():
    N, Q = map( int,input().split())
    C = list(map( lambda x: int(x)-1, input().split()))
    # 0 OR 1 WARNING
    Queries = [ tuple(map( lambda x: int(x)-1, input().split())) for _ in range(Q)]
    class_of_i = [defaultdict(int) for _ in range(N)]
    for i, c in enumerate(C):
        class_of_i[i][c] = 1
    A = [ i for i in range(N)]
    ANS = []
    for p, x, y in Queries:
        if p == 0:
            s, t = find(A,x), find(A,y)
            if s == t:
                continue
            if s > t:
                s, t = t, s
            union(A,s,t)
            for key in class_of_i[t].keys():
                class_of_i[s][key] += class_of_i[t][key]
        else:
            ANS.append(class_of_i[find(A,x)][y])

    print("\n".join(map(str, ANS)))
if __name__ == '__main__':
    main()
