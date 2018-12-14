N = int(input())
for i in range(8):
    if 2**i > N:
        break
print(2**(i-1))
