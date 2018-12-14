d, n = map(int, input().split())
if n == 100:
    print("{}".format(100**(d + 1) + 100**d))
else:
    print("{}".format(n*(100**d)))
