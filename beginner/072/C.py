from collections import Counter
N = int(input())
A = list( map( int, input().split()))
CA = Counter(A)
ans = 0
for i in range(1,10**5):
    ans = max( ans, CA[i-1]+CA[i]+CA[i+1])
print(ans)
    









