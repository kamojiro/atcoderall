L = list(input())
R = list(input())
L_reverse = L[::-1]
R_reverse = R[::-1]
if L == R_reverse and R == L_reverse:
    print('YES')
else:
    print('NO')
    
