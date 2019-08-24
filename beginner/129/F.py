#import sys
#input = sys.stdin.readline
#from numpy import matrix, eye, dot
def productMatrix(N, A, B):
    Ret = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Ret[i][j] += A[i][k]*B[k][j]
    return Ret
def modMatrix(N, A, Q): #N×N行列のmod
    for i in range(N):
        for j in range(N):
            A[i][j] %= Q
#            A[i,j] %= Q
    return

def powOfMatrix(N, X, n, Q): #N×N行列のn乗
#    Ret = eye(N)
    Ret = [[1,0,0],[0,1,0],[0,0,1]]
    power = '{:060b}'.format(n)[::-1] #log2(pow(10,18)) < 60
    for p in power:
        if p == "1":
            Ret = productMatrix(N,Ret, X)
#            Ret = dot(Ret, X)
            modMatrix(N, Ret, Q)
        X = productMatrix(N,X,X)
#        X = dot(X,X)
        modMatrix(N, X, Q)
#        print(Ret)
    return Ret

def main():
    L, A, B, M = map( int, input().split())
    s = A
    ANS = [[1,0,0],[0,1,0],[0,0,1]]
    for i in range(1, 37):
#        print(i, ANS)
        if s >= pow(10,i):
            continue
        P = [[pow(10, i, M), 0, 0], [1,1,0], [0,B,1]]
#        P = matrix([[pow(10, i, M), 0, 0], [1,1,0], [0,B,1]])
#        print((pow(10,i)-1-s)//B+1)
        step = (pow(10,i)-s+B-1)//B
        if L <= step:
            ANS = productMatrix(3,ANS,powOfMatrix(3,P,L,M))
#            ANS = dot(ANS,powOfMatrix(3,P,L,M))
            modMatrix(3,ANS,M)
            break
#        print(powOfMatrix(3,P, (pow(10,i)-1-s)//B + 1,M))
        ANS = productMatrix(3,ANS, powOfMatrix(3,P, step,M))
#        ANS = dot(ANS, powOfMatrix(3,P, (pow(10,i)-1-s)//B + 1,M))
#        print( (ANS[1][0]*A + ANS[2][0])%M, (pow(10,i)-1-s)//B + 1)
        modMatrix(3,ANS, M)
        L -= step
        s += step*B
    print( (ANS[1][0]*A + ANS[2][0])%M)
#    print( int((ANS[1,0]*A + ANS[2,0])%M))
        
        
if __name__ == '__main__':
    main()
