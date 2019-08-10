import sys
input = sys.stdin.readline

def main():
    N = int( input())
    S = [ list(input()) for _ in range(N)]
    for i in range(N):
        S[i] = "".join(sorted(S[i][:10]))
    S.sort()
    cnt = 1
    ans = 0
    now = S[0]
    for i in range(1, N):
        if now == S[i]:
            cnt += 1
            continue
        ans += cnt*(cnt-1)//2
        cnt = 1
        now = S[i]
    ans += cnt*(cnt-1)//2
    print(ans)
    
if __name__ == '__main__':
    main()
