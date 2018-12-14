A, B, K = map(int, input().split())
K = min(K,B-A+1)
S = set()
for i in range(K):
    S.add(A + i)
for i in range(K):
    S.add(B - i)
L = sorted(list(S))
for x in L:
    print(x)

    
