S = sorted(list(input()))
T = sorted(list(input()))
s = ''
t = ''
for i in S:
    s += i
for j in T:
    t = j + t
if s < t:
    print('Yes')
else:
    print('No')
    
