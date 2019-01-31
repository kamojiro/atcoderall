#2025
c = 2025 - int( input())
for i in range(1,10):
    for j in range(1,10):
        if i*j == c:
            print( str(i) + " x " + str(j))
