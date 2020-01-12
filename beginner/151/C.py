#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    PS = [tuple( input().split()) for _ in range(M)]
    AC = [False]*(N+1)
    C = [0]*(N+1)
    for p, s in PS:
        p = int( p)
        if AC[p]:
            continue
        if s == "AC":
            AC[p] = True
        else:
            C[p] += 1
    ansac = 0
    anspena = 0
    for i in range(N+1):
        if AC[i]:
            ansac += 1
            anspena += C[i]
    print(ansac, anspena)
    
if __name__ == '__main__':
    main()
