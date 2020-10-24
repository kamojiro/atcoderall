#import sys
#input = sys.stdin.readline
Q = 10**9+7



def main():
    H, W = map(int,input().split())
    S = [list(input()) for _ in range(H)]

    Lites = [[0]*W for _ in range(H)]
    K = 0
    for i in range(H):
        nums = 0
        for j in range(W):
            if S[i][j] == "#":
                nums = 0
                continue
            K += 1
            nums += 1
            Lites[i][j] = nums
        now = -1
        for j in range(W-1,-1,-1):
            if Lites[i][j] == 0:
                now = -1
                continue
            if now == -1:
                now = Lites[i][j]
            else:
                Lites[i][j] = now
    TateLites = [[0]*W for _ in range(H)]
    for j in range(W):
        nums = 0
        for i in range(H):
            if S[i][j] == "#":
                nums = 0
                continue
            nums += 1
            TateLites[i][j] = nums
        now = -1
        for i in range(H-1,-1,-1):
            if TateLites[i][j] == 0:
                now = -1
                continue
            if now == -1:
                now = TateLites[i][j]
            else:
                TateLites[i][j] = now
    
    pows = [1]
    pows = [1]
    for _ in range(K):
        pow2.append(pows[-1]*2%Q)
    

    for _ in range(K):
        pow2.append(pows[-1]*2%Q)


    pow2 = [1]
    for _ in range(K+1):
        pow2.append(pow2[-1]*2%Q)
    
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            p = Lites[i][j]+TateLites[i][j]-1
            ans += (pow2[p]-1)*pow2[K-p]%Q
            ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()
