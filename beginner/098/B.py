N = int(input())
*S, = list(input())
A = [chr(i) for i in range(97, 97+26)]
K = 0
for L in range(1,N):
    cnt = 0
    for alpha in A:
        if alpha in S[:L] and alpha in S[L:]:
            cnt += 1
    K = max(K,cnt)
print(K)
