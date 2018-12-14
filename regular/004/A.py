from itertools import combinations
N =int(input())
X = [list(map(int,input().split())) for i in range(N)]
ans = 0
for z in combinations(range(N),2):
    i,j = z[0],z[1]
    ans = max( ans, (X[i][0] - X[j][0])**2 + (X[i][1] - X[j][1])**2)
print(ans**(1/2))









