#import sys
#input = sys.stdin.readline
def main():
    H, W = map( int, input().split())
    B = [input()+"#" for _ in range(H)] + [["#"]*(W+1)]
    F = [[False]*(W+1) for _ in range(H)] + [[False]*(W+1)]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if B[i][j] == '#':
                continue
            if B[i+1][j] == '#' and B[i][j+1] == '#' and B[i+1][j+1] == '#':
                continue
            if B[i+1][j] == '.':
                F[i][j] |= not F[i+1][j]
            if B[i][j+1] == '.':
                F[i][j] |= not F[i][j+1]
            if B[i+1][j+1] == '.':
                F[i][j] |= not F[i+1][j+1]
            # if B[i+1][j] == '.':
            #     S[i][j] &= F[i+1][j]
            # if B[i][j+1] == '.':
            #     S[i][j] &= F[i][j+1]
            # if B[i+1][j+1] == '.':
            #     S[i][j] &= F[i+1][j+1]
    if F[0][0]:
        print("First")
    else:
        print("Second")
if __name__ == '__main__':
    main()
