N = int( input())
L = input()
ans = 0
for i in range(N):
    if L[i] == "A":
        ans += 4
    elif L[i] == "B":
        ans += 3
    elif L[i] == "C":
        ans += 2
    elif L[i] == "D":
        ans += 1
print( ans/N)










