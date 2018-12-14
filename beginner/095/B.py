N, X = map(int,input().split())
A = []
for i in range(N):
    A += [int(input())]
SUM = sum(A)
MIN = min(A)
print(int(N + (X - SUM)//MIN))
    









