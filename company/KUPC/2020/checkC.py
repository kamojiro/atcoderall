#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    ans = set()
    # for i in range(N):
    #     t = S[i][-1]
    #     for j in range(N-2,-1,-1):
    #         t = S[i][j]+t
    #         ans.add(t)
    # for j in range(N):
    #     t = S[-1][j]
    #     for i in range(N-2,-1,-1):
    #         t = S[i][j]+t
    #         ans.add(t)
    duplicate = defaultdict(lambda:1)
    for i in range(N):
        for j in range(N-1):
            for k in range(j+2,N+1):
                word = "".join(S[i][j:k])
                if word in ans:
                    duplicate["".join(S[i][j:k])] += 1
                ans.add(word)
                
    TS = list(zip(*S))
    # print(TS)
    for i in range(N):
        for j in range(N-1):
            for k in range(j+2,N+1):
                word = "".join(TS[i][j:k])
                if word in ans:
                    duplicate["".join(S[i][j:k])] += 1
                ans.add(word)

    # print(ans)
    print("N^2*(N-1)", N**2*(N-1))
    print(len(ans))
    if len(ans) < N**2*(N-1):
        print(duplicate)
    
if __name__ == '__main__':
    main()
