#import sys
#input = sys.stdin.readline
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
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    sa = sum(A)
    R = factors(sa)
    l = len(R)
    E = [0]*l
    ans = 0
    for r in R:
        cnt = 0
        E = list( map( lambda x:x%r, A))
        E.sort()
        s = sum(E)
        now = 0
        if s - E[-1] <= K:
            if ans < r:
                ans = r
            continue
        if s == 0:
            continue
        v = 0
        w = N-1
        cnt = 0
        while w-v != 0:
            if E[v] == 0:
                v += 1
                continue
            if E[w] == 0:
                w -= 1
                continue
            if E[v] + E[w] >= r:
                E[v] -= r - E[w]
                cnt += r - E[w]
                E[w] = 0
                w -= 1
            else:
                E[w] += E[v]
                cnt += E[v]
                E[v] = 0
                v += 1
        if cnt <= K:
            if r > ans:
                ans = r
    print(ans)
if __name__ == '__main__':
    main()
