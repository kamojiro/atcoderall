#import sys
#input = sys.stdin.readline
def main():
    A, B = map(int, input().split())
    # A -> 0, B -> 1
    N = 100
    S = [["#"]*N for _ in range(N//2)] + [["."]*N for _ in range(N//2,N)]
    a = A-1
    b = B-1
    for i in range(1,N//2-1,2):
        for j in range(0,N,2):
            if a > 0:
                S[i][j] = "."
                a -= 1
            else:
                break
        if a <= 0:
            break
    for i in range(N//2+1,N,2):
        for j in range(0,N,2):
            if b > 0:
                S[i][j] = "#"
                b -= 1
            else:
                break
        if b <= 0:
            break
    print(N,N)
    print("\n".join(["".join(S[i]) for i in range(N)]))
if __name__ == '__main__':
    main()
