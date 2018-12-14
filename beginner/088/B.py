N = int(input())
A = list(map(int,input().split()))
A = sorted(A,reverse = True)
Alice = 0
Bob = 0
for i in range(N):
    if i%2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]
print(Alice - Bob)
        
