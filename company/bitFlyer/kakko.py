def kakko(T):
    l = len(T)
    if l%2 == 1:
        return False
    else:
        s = int(l/2)
        T1 = T[:s]
        T2 = T[s:]
        T2 = T2[::-1]
        T2 = T2.replace('(','a').replace(')','(').replace('a',')')
        if T1 == T2:
            return True
        else:
            return False

def kkakko(U):
    l = len(U)
    if l%2 == 1:
        return False
    else:
        s = int(l/2) + 1
        i = 1
        while i <= s and  l != 0:
            if kakko(U[:i*2]) == True:
                U = U[i*2:]
                i = 1
                l = len(U)
                s = int(l/2) + 1
            else:
                i += 1
        if l == 0:
            return True
        else:
            return False

S = input()
c = 0
l = len(S)
s = l + 1
for i in range(l):
    for j in range(i+1, s):
        if kkakko(S[i:j]) == True:
            print("{}""{}".format(i,j))
            c += 1
print(c)

    
