N = list(input())
if N[0] == N[1] and N[1] == N[2]:
    print('Yes')
elif N[1] == N[2] and N[2] == N[3]:
    print('Yes')
else:
    print('No')
