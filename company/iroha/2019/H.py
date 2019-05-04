N = input()
S = sum( list( map( int, str(N))))
ans = ""
while S > 0:
    if S >= 9:
        ans = "9" + ans
        S -= 9
    else:
        ans = str(S) + ans
        break
if N == ans:
    if ans[0] == "9":
        ans = "18" + ans[1:]
    elif len(ans) == 1:
        ans = "1" + str( int(ans)-1)
    else:
        a, b = int(ans[0]), int( ans[1])
        a += 1
        b -= 1
        ans = str(a) + str(b) + ans[2:]
print(ans)
