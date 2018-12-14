n, m , d = map(int, input().split())
A = [0]*n
for i in range(1,m):
    B = A
    A = [0]*n
    for j in range(n):
        for k in range(n):
            if k + 1 - d >= 0 and k + 1 + d <= n:
                A[j] = B[j] + 2
            elif k + 1 - d >= 0 and k + 1 + d > n:
                A[j] = B[j] + 1
            elif k + 1 - d < 0 and k + 1 + d <= n:
                A[j] = B[j] + 1
            if k + 1 - d >= 0 and k + 1 + d <= n:
                A[j] += 2
            elif k + 1 - d >= 0 and k + 1 + d > n:
                A[j] += 1
            elif k + 1 - d < 0 and k + 1 + d <= n:
                A[j] += 1
print(sum(A)/(n**m))
            
                
            
            
        
    
