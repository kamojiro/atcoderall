#import sys
#input = sys.stdin.readline
def get_accumulation(A,a,c,b,d): # x=a~c, y=b~d
    return A[c][d] - A[a-1][d] - A[c][b-1] + A[a-1][b-1]

def main():
    H, W = map( int, input().split())
    C = [ list( map( int, input().split())) for _ in range(H)]
    
    # 2-dimensional accumulation
    AC = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            AC[i+1][j+1] = AC[i+1][j] + C[i][j]*pow(-1,i+j)
    for j in range(W):
        for i in range(H):
            AC[i+1][j+1] += AC[i][j+1]
    # C(H,2)*C(W,2) ≒ 10**8
    ans = 0
    for a in range(1,H+1):
        for c in range(a, H+1):
            for b in range(1,W+1):
                for d in range(b,W+1):
                    if get_accumulation(AC,a,c,b,d) == 0:
                        if ans < (c-a+1)*(d-b+1):
                            ans = (c-a+1)*(d-b+1)
    print(ans)
    
if __name__ == '__main__':
    main()
