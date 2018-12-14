N = int( input())
cake = '.'*N
ANS = ['']*N
for i in range(N):
    if i%2 == 1:
        ANS[i] = cake
    else:
        ans = ''
        if i%4 == 0:
            for j in range(N):
                if j%3 == 1:
                    ans += 'X'
                else:
                    ans += '.'
        else:
            for j in range(N):
                if j%3 == 1:
                    ans += '.'
                else:
                    ans += 'X'
        ANS[i] = ans
if (N-1)%2 == 1:
    
    
for i in range(N):
    print(ANS[i])
