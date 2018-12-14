S = input()
A = []
ans = 'yes'
for s in S:
    if s in A:
        ans = 'no'
        break
    A.append(s)
print(ans)
    
