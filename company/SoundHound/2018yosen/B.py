S = input()
LS = list(S)
w = int(input())
c = LS[0]
l = 1
while l*w + 1 <= len(S):
    c += LS[l*w]
    l += 1
print(c)
