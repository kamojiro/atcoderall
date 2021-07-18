#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    ANS = [[0]*(N-1) for _ in range(2)]
    for p in range(2**(N-1)):
        z = False
        t = p
        s = False
        for i in range(N-1):
            if t%2 == 0:
                if z:
                    s = True
                    break
                z = True
            else:
                z = False
            t //= 2
        if s:
            continue
        t = p
        for i in range(N-1):
            ANS[t%2][i] += 1
            t //= 2
    for i in range(N-1):
        print(i,": +",  ANS[1][i],"-", ANS[0][i])

        
if __name__ == '__main__':
    main()
