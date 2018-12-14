N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B = B[::-1]
SumA, SumB = [0],[0]
for i in range(N):
    SumA.append(SumA[-1] + A[i])
    SumB.append(SumB[-1] + B[i])
ans = 0
for i in range(N):
    ans = max(ans, SumA[i+1]+SumB[N-i])
print(ans)










