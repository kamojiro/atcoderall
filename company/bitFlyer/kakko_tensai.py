S = input()

ans = 0
stack = [1]
for c in S:
    if c == '(':
        stack.append(1)
        print(stack)
    else:
        if len(stack) == 1:
            stack[-1] = 1
            print(stack)
        else:
            stack.pop()
            ans += stack[-1]
            stack[-1] += 1
            print(stack)
            print(ans)

print(ans)








