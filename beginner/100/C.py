def prime(x):
    c = 0
    while x%2 == 0:
        x = x/2
        c += 1
    return c
n = int(input())
nums = input().split()
c = 0
for i in nums:
    c += prime(int(i))
print(c)
