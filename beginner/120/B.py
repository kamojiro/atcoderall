a, b, k = map( int, input().split())
T = []
for i in range(1,101):
    if a%i == 0 and b%i == 0:
        T.append(i)
print(T[-k])
