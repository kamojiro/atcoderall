def fact2(a, b):
    c2 = 0
    c5 = 0
    while a%2 == 0:
        a //= 2
        c2 += 1
    while a%5 == 0:
        a //= 5
        c5 += 1
    return min(c2-b, 9), min(c5-b,9)

def main():
    N = int( input())
    A2 = [0]*N
    A5 = [0]*N
    AS = [0]*N
    for i in range(N):
        a = input()
        if '.' in a:
            b, c = a.split('.')
            if int(c) == 0:
                pass
            else:
                c = str( int(c))
                AS[i] = len(c)
                b += c
        else:
            b = a
        # A2[i], A5[i] = fact( int(b))
        # print(b)
        A2[i], A5[i] = fact2( int(b), AS[i])

    R = [ [0]*19 for _ in range(19)]
    for i in range(N):
        a, b = A5[i]+9, A2[i]+9
        R[a][b] += 1
    AR = [ [0]*19 for _ in range(19)]
    for i in range(18,-1,-1):
        for j in range(17,-1,-1):
            R[i][j] = R[i][j] + R[i][j+1]
    for j in range(19):
        for i in range(17,-1,-1):
            R[i][j] += R[i+1][j]
    ans = 0
    print("\n".join( [" ".join( map( str, a)) for a in R]))
    for k in range(N):
        i, j = A5[k], A2[k]
        if i <= 9 and j <= 9:
            ans += R[-i+9][-j+9]
            print(-i,-j,R[-i+9][-j+9])
            
            # print(-i+9,-j+9)
        if AS[k] == 0:
            ans -= 1
    print(ans//2)

# 2
# 10.73741824 
# 3051.7578125
# 2**30, 2**15

if __name__ == '__main__':
    main()
