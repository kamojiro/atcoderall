T = int(input())
S = [ input() for _ in range(T)]
def cnt(K):
    L = len(K)
    if L < 5:
        return 0
    else:
        i = 0
        ans = 0
        while i <= L-5:
            if K[i:i+5] == 'kyoto' or K[i:i+5] == 'tokyo':
                i += 5
                ans += 1
            else:
                i += 1
        return ans
for j in range(T):
    print(cnt(S[j]))
