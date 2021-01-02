import sys
input = sys.stdin.readline
def main():
    N, M, Q = map( int, input().split())
    S = [ tuple( input().split()) for _ in range(Q)]
    Point = [N]*(M+1)
    Score = [[False]*(M+1) for _ in range(N+1)]
    for s in S:
        if len(s) == 2:
            score = 0
            n = int(s[1])
            for i in range(1,M+1):
                if Score[n][i]:
                    score += Point[i]
            print(score)
            continue
        n = int(s[1])
        m = int(s[2])
        Point[m] -= 1
        Score[n][m] = True

    
if __name__ == '__main__':
    main()
