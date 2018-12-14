def tansa(a, m):
    return {[(a[0]*10)%m, a[1]], [(a[0]+1)%m, a[1]+1]}    

K =int(input())
A = {[1,1]}
Flag = True
if K == 1:
    c = 1
else:
    while Flag == True:
        B = {[1,0]}
        for x in A:
            B = B|tansa(x,K)
        A = B
        C = [c[0] for c in A]
        if 0 in C:
            Flag = False
            
            break
        c += 1
        
print(c)










