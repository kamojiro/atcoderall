#import sys
#input = sys.stdin.readline
from collections import defaultdict, deque, Counter
def main():
    N, K = map( int, input().split())
    K %= 2*N
    A = list( map( int, input().split()))
    CA = Counter(A)
    q = deque()
    d = defaultdict( int)
    l = 1
    B = A+A
    C = []
    for i in range(N*2):
        b = B[i]
        if d[b] == 0:
            q.append((b,i))
            d[b] = 1
            continue
        d[b] = 0
        check = False
        if CA[b]%2 == 0:
            check = True
        while q:
            t, j = q.pop()
            d[t] = 0
            if t == b:
                if check == False:
                    break
                C.append(j)
                l += 1
                break
            else:
                if CA[t] != 1:
                    check = True
    if l == 0:
        print("")
        return
    k = K%l
    q = deque()
    d = defaultdict( int)
    if N%2 == 1:
        p = N
    for i in range(C[k], N*2):
        b = B[i]
        if d[b] == 0:
            q.append(b)
            d[b] = 1
            continue
        d[b] = 0
        while q:
            t = q.pop()
            d[t] = 0
            if t == b:
                break
    ANS = list(q)
    print( " ".join( map( str, ANS)))
    print(l, C)
if __name__ == '__main__':
    main()
