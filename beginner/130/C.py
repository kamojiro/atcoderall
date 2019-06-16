W, H, x, y = map( int, input().split())
if x*2 == W and y*2 == H:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)
