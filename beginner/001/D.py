from itertools import accumulate
N = int( input())
D = [0]*(24*12 + 2)
for _ in range(N):
    s, e = map( int, input().split("-"))
    sh = s//100
    sm = s-sh*100
    eh = e//100
    em = e - eh*100
    sm //= 5
    em = (em + 4)//5
    D[12*sh+sm] += 1
    D[12*eh+em] -= 1
AD = list(accumulate(D))
ans = ""
for i in range(24*12):
    if ans == "":
        if AD[i] > 0:
            ans += str(i//12*100 + (i-i//12*12)*5).zfill(4) + "-"
    else:
        if AD[i] <= 0:
            ans += str(i//12*100 + (i-i//12*12)*5).zfill(4)
            print( ans)
            ans = ""
if ans:
    ans += "2400"
    print( ans)
