N = int(input())
nums_s = input().split()
nums = [int(s) for s in nums_s]
nums_e = [s%2 for s in nums]
i = 0
while (nums_e.count(0) == N):
    nums = [s/2 for s in nums]
    nums_e = [s%2 for s in nums]
    i += 1
print(i)

#print(hoges)
#print("{}". format(N+N))
