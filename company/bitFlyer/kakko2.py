def kakko(S):
    l = len(S)
    if l%2 == 1:
        return False
    else:
        s = int(l/2)
        for i in range(s):
            S = S.replace("()", "")
        if S == "":
            return True
        else:
            return False

S = input()
c = 0
l = len(S)
s = l + 1
for i in range(l):
    for j in range(i+1, s):
        if kakko(S[i:j]) == True:
            c += 1
print(c)

