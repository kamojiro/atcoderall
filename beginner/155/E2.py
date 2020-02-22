#import sys
#input = sys.stdin.readline
def main():
    S = [ int(x) for x in input()]
    ans = 0
    N = len(S)
    l = 0
    r = 1
    d = dict()
    d[0] = 0
    d[1] = 1
    d[2] = 2
    d[3] = 3
    d[4] = 4
    d[5] = 5
    d[6] = 4
    d[7] = 3
    d[8] = 2
    d[9] = 1
    for i in range(N):
        if S[i] >= 5 and i < N-1:
            continue
        for s in range(l,i+1):
            if s == l and S[s] == 9:
                ans += 2
                continue
            ans += d[s]
        l = i
    print(ans)
            
if __name__ == '__main__':
    main()
