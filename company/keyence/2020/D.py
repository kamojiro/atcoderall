#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    if N == 1:
        print(0)
        return
    if N == 2:
        if A[0] <= A[1]:
            print(0)
            return
        if B[1] <= B[0]:
            print(1)
            return
        print(-1)
        return
    # even個なら良いはず
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
        
if __name__ == '__main__':
    main()
