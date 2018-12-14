A, B = map( int, input().split())
S = input()
ans = 'Yes'
R = [str(i) for i in range(10)]
for i in range(A):
    if S[i] in R:
        pass
    else:
        ans = 'No'
if S[A] == '-':
    pass
else:
    ans = 'No'
for i in range(B):
    if S[A+1+i] in R:
        pass
    else:
        ans = 'No'
print(ans)
