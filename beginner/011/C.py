n = int( input())
ng = [ int( input()) for _ in range(3)]
ans = "NO"
if not n in ng:
    for _ in range(100):
        if n == 1 or n == 2 or n == 3:
            ans = "YES"
            break
        if not n - 3 in ng:
            n -= 3
        elif not n - 2 in ng:
            n -= 2
        elif not n - 1 in ng:
            n -= 1
        else:
            break
print( ans)
        

