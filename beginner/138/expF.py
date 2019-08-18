#import sys
#input = sys.stdin.readline
def main():
    N = 50
    A = [["x"]*N for _ in range(N)]
    cnt = 0
    for i in range(1, N+1):
        print(i, bin(i)[2:], end = " | ")
        for j in range(i,N+1):
            if j%i == i^j:
                print(bin(j)[2:], end = " ")
                cnt += 1
                A[i-1][j-1] = "o"
        print(" |", cnt)
    print( " ".join( map( str, [i+1 for i in range(N)])))
    for i in range(N):
        print(" ".join(A[i]))
        
    # for n in range(1,N):
    #     cnt = 0
    #     for i in range(1,n+1):
    #         for j in range(i, n+1):
    #             if j%i == i^j:
    #                 cnt += 1
    #     print(n, cnt)
if __name__ == '__main__':
    main()
