N = input()
LN = list(N)
LN = [int(x) for x in LN]
if int(N)%sum(LN) == 0:
    print('Yes')
else:
    print('No')
