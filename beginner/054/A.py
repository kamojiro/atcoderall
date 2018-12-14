A, B = map( int, input().split())
if A == 1:
    A += 13
if B == 1:
    B += 13
if A > B:
    print('Alice')
elif A == B:
    print('Draw')
else:
    print('Bob')
