#import sys
#input = sys.stdin.readline
def main():
    A = [ list( map( int, input().split())) for _ in range(3)]
    N = int( input())
    B = [ int( input()) for _ in range(N)]
    T = [[0]*3 for _ in range(3)]
    for b in B:
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    T[i][j] = 1
    ans = 'No'
    for i in range(3):
        if T[i][0]*T[i][1]*T[i][2] > 0:
            ans = 'Yes'
    for i in range(3):
        if T[0][i]*T[1][i]*T[2][i] > 0:
            ans = 'Yes'
    if T[0][0]*T[1][1]*T[2][2] > 0:
        ans = 'Yes'
    if T[0][2]*T[1][1]*T[2][0] > 0:
        ans = 'Yes'
    print(ans)
if __name__ == '__main__':
    main()
