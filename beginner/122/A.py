b = input()
ans = ""
for s in b:
    if s == 'A':
        ans += 'T'
    elif s == 'T':
        ans += 'A'
    elif s == 'C':
        ans += 'G'
    else:
        ans += 'C'
print(ans)
