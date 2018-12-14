K = int(input())
kyu = ""
c = 0
e = 1
while c < K:
    while e < 10 and c < K:
        print(int(str(e) + kyu))
        c += 1
        e += 1
    e = 1
    kyu += "9"
        



