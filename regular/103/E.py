s = input()
n = len(s)
if s[0] == '1' and s[-1] == '0' and s[:n//2] == s[(n-1)//2:-1][::-1]:
    q = []
    now = 0
    for i in range(n):
        m = s[i]
        if m == '1':
            now = str(i+1)
            while q:
                print( q.pop() + ' ' + now)
        q.append( str(i+1))
    while q:
        a = q.pop()
        if now != a:
            print( a + ' ' + now)
else:
    print(-1)

