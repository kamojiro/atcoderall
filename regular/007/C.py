#import sys
#input = sys.stdin.readline
from itertools import product
from collections import Counter
def main():
    C = input()
    idx = 0
    P = [0]*10
    for c in C:
        if c == "o":
            P[idx] = 1
        idx += 1
    N = L = len(C)
    ans = N
    for Q in product(range(2), repeat=N):
        ANS = [0]*N
        for i in range(N):
            if Q[i] == 0:
                continue
            for j in range(N):
                if P[j] == 1:
                    ANS[(i+j)%N] = 1
        # print(Q, ANS, sum(ANS), Counter(Q)[1])
        if sum(ANS) == N:
            if Counter(Q)[1] < ans:
                ans = Counter(Q)[1]
    print(ans)
        
    
if __name__ == '__main__':
    main()
