S = list( input())
alphabets = [ 0 for _ in range(26)]
for x in S:
    alphabets[ord(x)-97] = 1
ans = 'None'
for i in range(26):
    if alphabets[i] == 0:
        ans = chr(i+97)
        break
print(ans)
