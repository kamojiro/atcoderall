#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map(int, list( input())))
    P = [False]*N
    for i in range(N):
        if A[2**i] == 1:
            P[i] = True
    ans = True
    for x in range(2**N):
        now = True
        y = x
        for i in range(N):
            if y%2 == 1:
                if not P[i]:
                    now = False
                    break
            y //= 2
        if (A[x] == 1 and not now) or ( A[x] == 0 and now):
            ans = False
            break
    if ans:
        print("Possible")
    else:
        print("Impossible")
        return
    L = 0
    ANS = ["0 0"]

    for i in range(N):
        if not P[i]:
            ANS.append( str(i) + " " + str(1))
            ANS.append( str(i+1) + " " + str(1))
            ANS.append( str(i+1) + " " + str(0))
            L += 3
        else:
            ANS.append( str(i+1) + " " + str(0))
            L += 1
    for i in range(N):
        ANS.append( str(N-1-i) + " " + str(0))
        L += 1
    print(L)
    print("\n".join(ANS))
            
if __name__ == '__main__':
    main()
