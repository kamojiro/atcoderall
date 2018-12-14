N = int( input())
A = list( map( int, input().split()))
zero = 0
ni = 0
yon = 0
for a in A:
    if a%2 == 1:
        zero += 1
    elif not a%4 == 0:
        ni += 1
    else:
        yon += 1
if ni == 0:
    if yon + 1 >= zero:
        print('Yes')
    else:
        print('No')
else:
    if yon >= zero:
        print('Yes')
    else:
        print('No')
    
