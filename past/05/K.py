#import sys
#input = sys.stdin.readline
from itertools import combinations

def exists(x,p):
    if (x & p) == p:
        return True
    else:
        return False

def main():
    S = [ list( input()) for _ in range(4)]
    P = [ pow(2,i) for i in range(16)]
    occupied = 0
    for i in range(4):
        for j in range(4):
            if S[i][j] == "#":
                occupied += P[i*4+j]
    dp = [0]*(2**16)
    for r in range(1,17):
        for c in combinations(range(16),r):
            y = sum( [P[p] for p in c ])
            e = 10**5
            for x in range(16):
                sharp = 0
                s = 0
                i, j = x//4, x%4
                if exists(y, P[x]):
                    sharp += 1
                    s += dp[y-P[x]]

                if i > 0:
                    if exists(y, P[(i-1)*4+j]):
                        sharp += 1
                        s += dp[y-P[(i-1)*4+j]]
                if i < 4-1:
                    if exists(y, P[(i+1)*4+j]):
                        sharp += 1
                        s += dp[y-P[(i+1)*4+j]]
                if j > 0:
                    if exists(y, P[i*4+j-1]):
                        sharp += 1
                        s += dp[y-P[i*4+j-1]]
                if j < 4-1:
                    if exists(y, P[i*4+j+1]):
                        sharp += 1
                        s += dp[y-P[i*4+j+1]]
                if sharp == 0:
                    continue
                f = (s+5)/sharp

                if f < e:
                    e = f
            dp[y] = e
    print(dp[occupied])

            
            


    
if __name__ == '__main__':
    main()
