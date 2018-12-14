from collections import Counter
N, K = map(int,input().split())
A = list(map(int,input().split()))
CA = Counter(A)
values, counts = zip(*CA.most_common())
counts = counts[::-1]
LA = len(CA)
L = max(LA - K,0)
ans = 0
for i in range(L):
    ans += counts[i]
print(ans)
