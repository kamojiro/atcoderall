a = int(input())
if a < 100:
    VV = 0
elif a >= 100 and a <= 5000:
    VV = a/100
elif a >= 6000 and a <= 30000:
    VV = a/1000 + 50
elif a >= 35000 and a <= 70000:
    VV = (a/1000 - 30)/5 +80
elif a > 70000:
    VV = 89

VV = int(VV)
if VV <= 9:
    VV = str(VV)
    VV = "0" + VV
else:
    VV = str(VV)
print(VV)
