from collections import Counter
S = Counter(input())
if S['a'] >= 1 and S['b'] >= 1 and S['c'] >= 1:
    print('Yes')
else:
    print('No')
