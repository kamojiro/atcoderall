#import sys
#input = sys.stdin.readline
def main():
    N, P = map( int ,input().split())
    S = [ int(s) for s in list(input())][::-1]
    L = [0]*P
    L[0] = 1
    t = 0
    for i in range(N):
        t = (S[i]*pow(10,i,P)+t)%P
        print(t)
        L[t] += 1
    ans = 0
    for l in L:
        ans += l*(l-1)//2
    print(ans)
    
if __name__ == '__main__':
    main()
