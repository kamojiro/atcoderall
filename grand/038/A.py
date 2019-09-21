#import sys
#input = sys.stdin.readline
def main():
    H, W, A, B = map( int, input().split())
    ANS = [ ['0']*W for _ in range(H)]
    now = 0
    A2 = 2*A
    B2 = 2*B
    if A == 0:
        for _ in range(B):
            print('1'*W)
        for _ in range(H-B):
            print('0'*W)
        return
    if B == 0:
        ans = '1'*A + '0'*(W-A)
        for _ in range(H):
            print(ans)
        return
            
    for i in range(H):
        if i >= B2:
            now = 0
        elif i % B2 >= B:
            now = A
        else:
            now = 0
        for j in range(W):
            if j >= A2:
               if now == 0:
                   ANS[i][j] = '1'
            elif (j+now)%A2 < A:
                ANS[i][j] = '1'
    for i in range(H):
        print( ''.join(ANS[i]))
if __name__ == '__main__':
    main()
