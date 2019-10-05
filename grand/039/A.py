#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    S = input()
    K = int( input())
    CS = Counter(S)
    if CS[ S[0]] == len(S):
        print( len(S)*K//2)
        return
    N = len(S)

    for i in range(N-1):
        if S[i] != S[i+1]:
            check = i+1
            break

    T = S[check:] + S[:check]
    ans = 0
    now = S[0]
    cnt = 1

    for t in S[1:check]:
        if now == t:
            cnt += 1
            continue
        ans += cnt//2
        cnt = 1
        now = t
    ans += cnt//2

    cnt = 1
    now = S[check]
    for t in S[check+1:]:
        if now == t:
            cnt += 1
            continue
        ans += cnt//2
        cnt = 1
        now = t
    ans += cnt//2
    
    cnt = 1
    now = T[0]
    cc = 0

    for t in T[1:]:
        if t == now:
            cnt += 1
            continue
        cc += cnt//2
        cnt = 1
        now = t
    cc += cnt //2
    ans += cc*(K-1)
    
    print(ans)
        
    
if __name__ == '__main__':
    main()
