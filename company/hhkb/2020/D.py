#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    T = int(input())
    NAB = [tuple(map(int,input().split())) for _ in range(T)]
    ANS = []
    for n, a, b in NAB:
        if n < a+b:
            ANS.append(0)
            continue
        ans = (n-a-b+1)*(n-a-b+2)%Q*(n-a+1)%Q*(n-b+1)%Q
        # print("ans",ans)
        # print("-",((n-a-b+1)*(n-a-b+2)//2%Q)**2%Q*2%Q)
        ans -=((n-a-b+1)*(n-a-b+2)//2%Q)**2%Q*2%Q
        ANS.append(ans%Q*2%Q)
    print("\n".join(map(str,ANS)))
        
if __name__ == '__main__':
    main()
