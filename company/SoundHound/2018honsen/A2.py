C, D = map( int, input().split())
m = C//140
M = D//170
ans = 0
L = []
for i in range(1,6):
    L.append(140*i)
    L.append(170*i)
S = [30*i for i in range(1,6)]
ans = 0
Flag = True
k = 6
for i in range(1,6):
    if 140*i <= C and C < 170*i:
        if D < 170*i:
            ans += D - C
            Flag = False
            break
        else:
            ans += 170*i - C
            k = i + 1
            break
    elif C >= 170*i and C < 140*(i+1):
        k = i+1

if Flag:
    for j in range(k,6):
        if D >= 170*(j-1) and D < 140*j:
            Flag = False
            break
        elif D >= 140*j and D < 170*j:
            ans += D - 140*j
            Flag = False
            break
        else:
            ans += 30*j

if Flag:
    ans += D-140*6

print(ans)
    
