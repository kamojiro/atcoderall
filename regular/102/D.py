L = int(input())
R = []
while L != 0:
    L, r = divmod(L,3)
    R.append(r)
M = 2
N = 0
l = 0
for i in R:
    M += int((3**(l-1))*i)
    N += l
    l += 1
print('{} {}'.format(20, M))
l = 0
cnt = 2
mark = 2
for i in R:
    now = 1
    K = list( range( mark, mark+l))
    for k in K:
        print()
    for j in range(l):
    l += 1
    
    
