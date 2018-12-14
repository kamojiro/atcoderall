import math
S = input()
c = len(S)
N = math.floor(c/5) + 1
S = S[::-1]
for i in range(N):
    if len(S) == 0:
        print("YES")
        break
    else:
        if S[:6] == "resare":
            S = S[6:]
        elif S[:7] == "remaerd":
            S = S[7:]
        elif S[:5] == "maerd" or S[:5] == "esare":
            S = S[5:]
        else:
            print("NO")
            break
else:
    print("NO")
    
##    s=input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
##    print("YES" if len(s)==0 else "NO")
