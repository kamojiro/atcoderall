s = input()
L = len(s)
for i in range(L):
    if s[i] == 'A':
        A = i
        break
for i in range(L-1,-1,-1):
    if s[i] == 'Z':
        Z = i
        break
print(Z-A+1)
