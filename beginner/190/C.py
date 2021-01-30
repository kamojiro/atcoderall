#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, M = map(int, input().split())
    AB = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(K)]
    ans = 0
    for P in product(range(2), repeat=K):
        S = [False]*N
        for i, cd in enumerate(CD):
            c, d = cd
            if P[i] == 0:
                S[c] = True
            else:
                S[d] = True
        now = 0
        for a, b in AB:
            if S[a] and S[b]:
                now += 1
        if now > ans:
            ans = now
    print(ans)
        
    
if __name__ == '__main__':
    main()
