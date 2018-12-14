x1, y1, x2, y2 = map( int, input().split())
if x1 <= x2:
    X = x2 - x1
    if y1 <= y2:
        Y = y2 - y1
        print("{} {} {} {}".format(x2-Y, y2+X, x1-Y, y1+X))
    else:
        Y = y1 - y2
        print("{} {} {} {}".format(x2+Y, y2+X, x1+Y, y1+X))
else:
    X = x1 - x2
    if y1 <= y2:
        Y = y2 - y1
        print("{} {} {} {}".format(x2-Y, y2 -X, x1-Y, y1-X))        
    else:
        Y = y1 - y2
        print("{} {} {} {}".format(x2+Y, y2-X, x1+Y, y1-X))
