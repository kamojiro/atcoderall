N = input()
NL = list(N)
SL = [int(i) for i in NL]
S = sum(SL)
N = int(N)
if N % S == 0:
    print("Yes")
else:
    print("No")






