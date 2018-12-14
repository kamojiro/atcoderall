N, K = map(int,input().split())
print((N-2)//(K-1)+1)
li = input().split()
n = li.index('1')
if n == 0:
    print((N-2)//(K-1) + 1)
elif n == N-1:
    print((N-2)//(K-1) + 1)
else:
    n += 1
    
