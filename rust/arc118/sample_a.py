#import sys
#input = sys.stdin.readline
def main():
    t = int( input())
    N = 1000
    A = [(t+100)*i//100 for i in range(N)]
    F = [True]*(N*(1+t))
    for a in A:
        F[a] = False
    ANS = [i for i in range(N) if F[i]]
    for i in range(len(ANS)):
        p = i+1
        if ANS[i] == ((100+t)*p-1)//t:
            continue
        else:
            print(i)
            print(ANS[i], ((100+t)*p-1)//p)
    print(ANS)
    


if __name__ == '__main__':
    main()
