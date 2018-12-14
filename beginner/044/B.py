w = input()
A = [0]*26
for v in w:
    A[ ord(v) - ord('a')] = ( A[ ord(v) - ord('a')] + 1)%2
if sum(A) > 0:
    print('No')
else:
    print('Yes')
