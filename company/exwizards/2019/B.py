from collections import Counter
N = int( input())
s = input()
r = Counter(s)["R"]
if r > N - r:
    print("Yes")
else:
    print("No")
