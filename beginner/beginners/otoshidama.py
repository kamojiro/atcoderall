n, y = map(int, input().split())
flag = False
for x in range(n+1):
    for z in range(n-x+1):
        if 10000*x + 5000*z + 1000*(n - x - z) == y:
            print("{} {} {}".format(x,z,n-x-z))
            flag = True
            break
    if flag:
            break
if flag == False:
    print("-1 -1 -1")

a
