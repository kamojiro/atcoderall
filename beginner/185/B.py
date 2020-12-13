#import sys
#input = sys.stdin.readline
def main():
    N, M, T = map( int, input().split())
    mN = N
    AB = [ tuple(map(int,input().split())) for _ in range(M)]
    AB.append((T,T))
    now = 0
    for a, b in AB:
        N -= a-now
        if N <= 0:
            print("No")
            return
        N += b-a
        N = min(N,mN)
        now = b
        # print(N)
    
    print("Yes")
if __name__ == '__main__':
    main()
