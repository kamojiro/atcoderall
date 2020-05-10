#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    A = list( map( lambda x: int(x)-1, input().split()))
    T = [0]
    C = [-1]*N
    C[0] = 0
    s = 0
    count = 0
    while True:
        s = A[s]
        count += 1
        if count == K:
            print(s+1)
            return
        if C[s] != -1:
            L = count - C[s]
            break
        C[s] = count
        T.append(s)

    m = len(T) - L
    print( T[-L:][(K-m)%L]+1)
if __name__ == '__main__':
    main()
