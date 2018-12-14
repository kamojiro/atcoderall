a, b, c, d, e, f = map( int, input().split())
ans = 0
ansL = 0
ansM = 0
for i in range(30//a+1):
    for j in range((30-i)//b+1):
        L = a*i + b*j
        M = 0
        for k in range(f):
            if 100*L + k*c <= f and k*c <= L*e:
                m = min(((e*L-k*c)//d)*d, ((f-100*L-k*c)//d)*d)
                M = max(M, m+k*c)
        if M+L != 0 and 100*L + M <= f and M <= L*e:
            if (M*100)/(M+L*100) > ans:
                ans = (M*100)/(M+L*100)
                ansL = L*100
                ansM = M
if ansL == 0:
    print('{} {}'.format(a*100,0))
else:
    print('{} {}'.format(ansL+ansM,ansM))
                    
