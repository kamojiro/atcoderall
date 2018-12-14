A, B = map( int, input().split())
Board = [ ['#']*100 for _ in range(50)] + [['.']*100 for _ in range(50)]
i = 0
nowj = 0
for _ in range(A-1):
    Board[i][nowj] = '.'
    if nowj == 98:
        nowj = 0
        i += 2
    else:
        nowj += 2
i = 51
nowj = 0
for _ in range(B-1):
    Board[i][nowj] = '#'
    if nowj == 98:
        nowj = 0
        i += 2
    else:
        nowj  += 2
print( '{} {}'.format(100, 100))
for i in range(100):
    print( ''.join(Board[i]))
