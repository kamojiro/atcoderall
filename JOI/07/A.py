from collections import Counter
n = int(input())
C = [input() for i in range(n)]
A = []
for i in range(n):
    if i%2 == 0:
        A.append(C[i])
    else:
        cnt = 1
        for j in range(i-1,-1,-1):
            if A[j] == C[i]:
                break
            else:
                A.pop(-1)
                cnt += 1
        for l in range(cnt):
            A.append(C[i])
print(Counter(A)['0'])
                
                
