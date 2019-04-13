N, K = map( int, input().split())
S = input()
l = 0
now = S[0]
k = 0
if now == "0":
    k = 1
r = 0
for i in range(1, N):
    if now == "1":
        if S[i] == "1":
            r = i
        else:
            k += 1
            if k > K:
                break
            r = i
            now = "0"
    else:
        r = i
        now = S[i]
ans = r - l + 1
while r < N - 1:
    if S[l] == "0":
        for i in range(l,N):
            if S[i] == "1":
                l = i
                break
    else:
        now = "1"
        for i in range(l, N):
            if now == "1":
                now = S[i]
            else:
                if S[i] == "1":
                    l = i
                    break
    now = "0"
    for i in range(r+1, N):
        if now == "0":
            now = S[i]
            r = i
        else:
            if S[i] == "0":
                r = i - 1
                break
            else:
                r = i
    if ans < r-l+1:
        ans = r-l+1
print(ans)
