N = int(input())
S = list(input())
S1 = S[:N]
S2 = S[2*N-1:N-1:-1]
 
dict_1 = dict()
q_list = [""]*(2**N)
res = 0
 
for i in range(2**N):
    sb = bin(2**N+i)[3:]
    red = []
    blue = []
    red2 = []
    blue2 = []
    for j in range(N):
        if sb[j]=="0":
            red.append(S1[j])
            red2.append(S2[j])
        else:
            blue.append(S1[j])
            blue2.append(S2[j])
    sss = "".join(red+["|"]+blue)
    sss2 = "".join(red2+["|"]+blue2)
    if sss not in dict_1.keys():
        dict_1[sss] = 1
    else:
        dict_1[sss] += 1
    q_list[i] = sss2
for q in q_list:
    res += dict_1.get(q, 0)
print(res)
