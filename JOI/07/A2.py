from collections import Counter
n = int(input())
C = [input() for i in range(n)]
A = [C[0]]
K = [0]*1000
for i in range(1,n):
    c = C[i]
    if i%2 == 0:#奇数
        A.append(c)
        if A[-2] == c:
            pass
        else:
            K.append(i)
    else:
        if A[-1] == c:
            A.append(c)
        else:
            k = K.pop()
            A = A[:k]
            for j in range(i-k+1):
                A.append(c)
print(Counter(A)['0'])
