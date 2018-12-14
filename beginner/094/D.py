n = int(input())
A = list(map(int, input().split()))
MA = max(A)
N = MA/2
X = max(A)-1
for i in range(n):
    if abs(A[i] - N) < X and A[i] != MA:
        X = abs(A[i] - N)
        k = i       
print('{} {}'.format(MA, A[k]))

