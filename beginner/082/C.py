from collections import Counter
N = int(input())
A = list(map(int,input().split()))
CA = Counter(A)
ans = 0
for x in CA:
    if CA[x] >= x:
        ans += CA[x] - x
    else:
        ans += CA[x]
print(ans)










