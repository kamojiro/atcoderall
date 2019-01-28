s = list( input())
l = len(s)
K = int( input())
for i in range(l-1):
    if s[i] == "a":
        continue
    if ord("z") - ord(s[i]) + 1 <= K:
        K -= ord("z") - ord(s[i]) + 1
        s[i] = "a"
s[l-1] = chr( ( ord(s[l-1]) - ord("a") + K)%26 + ord("a"))
print("".join(s))
