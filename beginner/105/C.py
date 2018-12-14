N = int(input())
fugou = 1
ans = ''
if N == 0:
    ans = '0'
else:
    q = N
    while q!= 0:
        if q > 0:
            r = q%2
            q = (-1)*(q//2)
        else:
            q = -q
            r = q%2
            if r == 0:
                q = q//2
            else:
                q = q//2+1
        ans += str(r)
print(ans[::-1])
