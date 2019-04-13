S = input()
ans0 = 0
ans1 = 0
N = len(S)
for i in range(N):
    if i%2 == 0:
        if S[i] == "0":
            ans1 += 1
        else:
            ans0 += 1
    else:
        if S[i] == "1":
            ans1 += 1
        else:
            ans0 += 1        
print(min(ans0, ans1))
