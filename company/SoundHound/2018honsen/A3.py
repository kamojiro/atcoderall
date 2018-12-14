C, D = map( int, input().split())
ans = 0
Flag = True
for i in range(45):
    ir = 2**i
    irp = 2**(i+1)
    if 140*ir <= C and C < 170*ir:
        if D-1 <= 170*ir:
            ans += D - C
            Flag = False
            break
        elif D - 1 == 170*ir:
            ans = 170*ir - C
            Flag = False
            break
        elif D == 170*ir:
            ans = 170*ir - C
            Flag = False
            break
        else:
            ans += 170*ir - C
            k = i + 1
            break
    elif C >= 170*ir and C < 140*irp:
        k = i+1
        break
else:
    Flag = False

if Flag:
    for j in range(k,45):
        jrq = 2**(j-1)
        jr = 2**j
        if D-1 < 140*jr:
            break
        elif D -1 >= 140*jr and D-1 < 170*jr:
            ans += D - 140*jr 
            break
        else:
            ans += 30*jr

print(ans)
