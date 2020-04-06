import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    N, M = map( int, input().split())
    X = list( map( int, input().split()))
    d = defaultdict( int)
    Same = [0]*M
    Mod = [0]*M
    for x in X:
        Mod[x%M] += 1
        if d[x] > 0:
            d[x] = 0
            Same[x%M] += 2
        else:
            d[x] += 1
    ans = 0
    ans += Mod[0]//2
    Mod[0] = Mod[0]%2
    if M%2 == 0:
        ans += Mod[M//2]//2
        Mod[M//2] = Mod[M//2]%2
    
    for i in range(1,(M+1)//2):
        m = min(Mod[i], Mod[-i])
        ans += m
        Mod[i] = Mod[i] - m
        Mod[-i] = Mod[-i] - m

    for i in range(M):
        ans += min(Mod[i], Same[i])//2
    print(ans)
    
if __name__ == '__main__':
    main()
