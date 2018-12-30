from collections import defaultdict
D = defaultdict( lambda : "")
D[(0,1)] = "Brown"
D[(0,0)] = "Brown"
D[(1,1)] = "Brown"
D[(1,0)] = "Brown"
for i in range(2, 100):
    for x in range(i//2+1):
        y = i-x
        if D[(x,y)] == "":
            which = "Brown"
            for j in range(1,x//2+1):
                if D[(x-j*2, y + j)] == "Brown":
                    which = "Alice"
                    break
            for j in range(1,y//2+1):
                if D[(x+j,y-j*2)] == "Brown":
                    which = "Alice"
                    break
            print(x,y,which)
            D[(x,y)] = D[(y,x)] = which
# L = [[""] for _ in range(100)]
# for i in range(100):
#     for j in range(i,100):
#         if not D[(i,j)] == "":
#             L[i].append(D[(i,j)])
##print(L)
