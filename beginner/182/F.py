#import sys
#input = sys.stdin.readline
def adic(n,A):
    ret = []
    for a in A:
        ret.append(n//a)
        n %= a
    return ret

def main():
    N, X = map(int,input().split())
    A = list(map(int,input().split()))
    RA = [ A[i] for i in range(N-1,-1,-1)]
    print(adic(X,RA))
             
    
    # X <= y <= X+A_N
if __name__ == '__main__':
    main()





