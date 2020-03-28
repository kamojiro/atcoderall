#import sys
#input = sys.stdin.readline
def main():
    N, X, Y = map( int, input().split())
    K = [0]*N
    X -= 1
    Y -= 1
    for i in range(N-1):
        for j in range(i+1,N):
            if i <= X:
                if j <= X:
                    K[j-i] += 1
                elif X <= j <= Y:
                    if (X-i) + 1 + (Y-j) <= j-i:
                        K[(X-i) + 1 + (Y-j)] += 1
                    else:
                        K[j-i] += 1
                else:
                    K[(X-i) + 1 + (j-Y)] += 1
            elif i <= Y:
                if j <= Y:
                    if (i-X) + 1 + (Y-j) <= j-i:
                        K[(i-X) + 1 + (Y-j)] += 1
                    else:
                        K[j-i] += 1
                else:
                    if (i-X) + 1 + (j-Y) <= j-i:
                        K[(i-X) + 1 + (j-Y)] += 1
                    else:
                        K[j-i] += 1
            else:
                K[j-i] += 1

    print( "\n".join( map( str, K[1:])))
if __name__ == '__main__':
    main()
