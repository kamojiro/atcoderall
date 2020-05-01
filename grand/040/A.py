#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = len(S)+1
    now = 0
    A = [0]
    for s in S:
        if s == "<":
            now += 1
        else:
            now = 0
        A.append(now)
    B = [0]
    now = 0
    for s in S[::-1]:
        if s == ">":
            now += 1
        else:
            now = 0
        B.append(now)
    B = B[::-1]
    ans = sum( [ max(A[i], B[i]) for i in range(N)])
    
    print(ans)
        
if __name__ == '__main__':
    main()
