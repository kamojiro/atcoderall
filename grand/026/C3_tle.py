N = int(input())
S = input()
dict_left = {}
S_left = S[:N]
S_right = S[2*N-1:N-1:-1]
for x in range(2**N):
    red_left = ''
    blue_left = ''
    B = bin(x)[2:]
    B = B.zfill(N)
    for i in range(N):
        if int(B[i]) == 1:
            red_left += S_left[i]
        else:
            blue_left += S_left[i]
    tango = red_left + '|' + blue_left
    if tango in dict_left:
        dict_left[tango] += 1
    else:
        dict_left[tango] = 1
ans = 0
for x in range(2**N):
    red_right = ''
    blue_right = ''
    B = bin(x)[2:]
    B = B.zfill(N)
    for i in range(N):
        if int(B[i]) == 1:
            red_right += S_right[i]
        else:
            blue_right += S_right[i]
    tango = blue_right + '|' + red_right
    if tango in dict_left:
        ans += dict_left[tango]

print(ans)

            
        
        
        
