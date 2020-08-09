def main():
    N = int( input())
    ANS = []
    for _ in range(N):
        a, b, c, d = input().split()
        if a == "<":
            ANS.append((0, int(b), int(c), int(d)))
        else:
            ANS.append((1, int(b), int(c), int(d)))
    ans = 0
    
    L = [0]*(100000)
    L[0] = 2
    L[1] = 3
    for t, i, j , k in ANS:
        x = L[i]
        y = L[j]
        if t == 0:
            if L[i] < L[j]:
                L[k] = 1
            else:
                L[k] = 0
        else:
            L[k] = L[i]+L[j]
        if t == 0:
            print(x,"<", y,"=", L[k])
        else:
            print(x,"+", y,"=", L[k])

if __name__ == '__main__':
    main()
