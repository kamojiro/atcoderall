N = int(input())
for i in range(N+2):
    if N < i**2:
        j = i - 1
        break
print(j**2)
