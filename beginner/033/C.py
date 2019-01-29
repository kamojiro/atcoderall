S = input()
previousnumber = "0"
ans = 0
times = 0
timesnow = 0
for s in S:
    if s == "*":
        if times == 0:
            timesnow = 1
            if previousnumber == "0":
                timesnow = 0
            times = 1
        else:
            if previousnumber == "0":
                timesnow = 0
                previousnumber = "0"
    elif s == "+":
        if times == 1:
            if previousnumber == "0":
                timesnow = 0
            if timesnow == 1:
                ans += 1
                timesnow = 0
            times = 0
            previousnumber = "0"
        if not previousnumber == "0":
            ans += 1
    else:
        previousnumber = s
if times == 1:
    if previousnumber == "0":
        timesnow = 0
    if timesnow == 1:
        ans += 1
else:
    if not previousnumber == "0":
        ans += 1
print( ans)
