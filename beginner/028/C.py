C = list( map( int, input().split()))
K =[]
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            K.append(C[i]+C[j]+C[k])
K = list( set(K))
K.sort(key=None, reverse=True)
print(K[2])
