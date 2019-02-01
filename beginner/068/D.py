K = int(input())
print(50)
s, t = K//50, K%50
ANS = [ s + i for i in range(50)]
for j in range(t):
    for i in range(50):
        if j == i:
            ANS[i] += 50
        else:
            ANS[i] -= 1
print(" ".join( map( str, ANS)))
