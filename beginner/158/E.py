# import sys
# input = sys.stdin.readline
def main():
    N, P = map( int ,input().split())
    S = [ int(s) for s in list(input().strip())][::-1]
    if P == 2 or P == 5:
        ans = 0
        for i in range(N):
            if S[i]%P == 0:
                ans += N-i
        print(ans)
        return
    L = [0]*P
    L[0] = 1
    t = 0
    s = 1
    for z in S:
        t = (z*s+t)%P
        L[t] += 1
        s = s*10%P
    ans = 0
    for l in L:
        ans += l*(l-1)//2
    print(ans)
    
if __name__ == '__main__':
    main()
