A = int( input())
B = int( input())
C = int( input())
S = int( input())
V = A+B+C
ans = 'No'
for i in range(4):
    if V+i == S:
        ans = 'Yes'
        break
print(ans)










