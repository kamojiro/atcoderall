from itertools import product
N = int( input())
ans = 0
for i in range(3,10):
    for x in product("357", repeat = i):
        z = ""
        V = [0]*10
        for l in x:
            z += l
            V[ int( l)] = 1
        if int(z) <= N and sum(V) == 3:
            ans += 1
print(ans)
