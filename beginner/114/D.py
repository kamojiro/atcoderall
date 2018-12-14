N = int( input())
W = [0]*101
for i in range(2,N+1):
    j = i
    for k in range(2,100):
        while j%k == 0:
            W[k] += 1
            j //= k
ans = 0
if N >= 78:
    ans += 1
for i in range(2,N+1):
    if W[i] >= 2:
        for j in range(2,N+1):
            if j == i:
                continue
            if W[j] >= 24:
                ans += 1
for i in range(2,N+1):
    if W[i] >= 4:
        for j in range(2,N+1):
            if j == i:
                continue
            if W[j] >= 14:
                ans += 1

for i in range(2,N+1):
    if W[i] >= 2:
        for j in range(2,N+1):
            if j == i:
                continue
            if W[j] >= 4:
                for k in range(j,N+1):
                    if k == i or k == j:
                        continue
                    if W[k] >= 4:
                        ans += 1

print(ans)
