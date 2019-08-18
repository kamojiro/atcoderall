#import sys
#input = sys.stdin.readline
Q = 10**9+7
def solve(T):
    if T == 0:
        return 0
    ret = 0
    r = 0
    now = 0
    t = 1
    for i in range(1,60):
        if pow(2,i) - 1 <= T:
            ret += pow(3,i,Q)
            ret %= Q
            now = pow(2,i,Q)
            r = i
        else:
            break
    cnt = T - now
    while i > 0:
        i -= 1
        if cnt < pow(2,i):
            pass
        else:
            ret += pow(3,i,Q)*pow(2,t,Q)%Q
            t += 1
        ret %= Q
    return ret
            
    


def main():
    L, R = map( int, input().split())
    print((solve(R) - solve(L-1))%Q)
if __name__ == '__main__':
    main()
