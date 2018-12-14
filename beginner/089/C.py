from collections import Counter
N = int(input())
T = [input() for i in range(N)]
S = [x[:1] for x in T]
CS = Counter(S)
A = [CS['M'],CS['A'],CS['R'],CS['C'],CS['H']]
ans = 0
for i in range(0,3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans += A[i]*A[j]*A[k]
print(ans)
            

