#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = set()
    A.add((0,0))
    for _ in range(N):
        B = set()
        for x, y in A:
            B.add((x+1,y))
            B.add((x, y+1))
            B.add((x+y,y))
            B.add((x,x+y))

        A = A.union(B)
        print(A)
    ans = set()
    for x,_ in A:
        ans.add(x)
    ans = sorted(list(ans))
    print(ans)
if __name__ == '__main__':
    main()
