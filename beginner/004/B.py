C = [ [] for _ in range(4)]
for i in range(4):
    C[i] = list( input().split())
for i in range(3,-1,-1):
    print( " ".join(C[i][::-1]))
