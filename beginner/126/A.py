N, K = map( int, input().split())
S = input()
ans = S[:K-1]
if S[K-1] == "A":
    ans += "a"
elif S[K-1] == "B":
    ans += "b"
else:
    ans += "c"
ans += S[K:]
print(ans)










