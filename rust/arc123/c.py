#import sys
#input = sys.stdin.readline
def main():
    M = 333
    K = 2
    A = [False]*(M*5+1);
    B = [1,2,3];
    for _ in range(K):
        Z = [];
        for i in range(1,4):
            for b in B:
                Z.append(b*10+i)
        B.extend(Z)
    N = 3
    ANS = [ b for b in B]
    for _ in range(N):
        Z = [];
        for ans in ANS:
            for b in B:
                Z.append(b+ans)
        ANS.extend(Z)
    for ans in ANS:
        A[ans] = True
    for i in range(1,M*5+1):
        if not A[i]:
            print(i)
if __name__ == '__main__':
    main()
