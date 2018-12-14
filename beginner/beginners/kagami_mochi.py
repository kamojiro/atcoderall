N = int(input())
mochies = list()
for i in range(N):
    d_i = int(input())
    mochies.append(d_i)
mochies = sorted(mochies)
c = 0
k = 0
for i in mochies:
    if i > k:
        c += 1
        k = i
print(c)
    
        


