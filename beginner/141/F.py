#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    mina = min(A)
    ans = 0
    for a in A:
        ans ^= a
    ans = ans^mina + mina
    red = [0]*N
    now = 0
    P = [0]*60
    for p in range(59,-1,-1):
        if P[59-p] == 1:
            continue
        print(p)
        a, t = -1, -1
        q = pow(2,p)
        q1 = pow(2,p+1)
        for i in range(N):
            if red[t] == 1:
                continue
            if A[i] >= q and A[i] < q1:
                if A[i] > a:
                    a = A[i]
                    t = i
        if a != -1:
            now ^= a
            power = '{:060b}'.format(a)
            red[t] = 1
            for i in range(60):
                if power[i] == "1":
                    P[i] = 1
            print(P)
    nowb = 0
    for i in range(N):
        if red[i] == 0:
            nowb ^= A[i]
    print( max( ans, now + nowb))
if __name__ == '__main__':
    main()
