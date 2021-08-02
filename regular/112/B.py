#import sys
#input = sys.stdin.readline
def main():
    B, C = map(int, input().split())
    L1 = B - C//2
    R1 = B + abs(C-2)//2
    L2 = - B - (C-1)//2
    R2 = - B + (C-1)//2
    if L2 <= L1 and L1 <= R2:
        a = min(L1,L2)
        b = max(R1,R2)
        print(b-a+1)
    elif L1 <= L2 and L2 <= R1:
        a = min(L1,L2)
        b = max(R1,R2)
        print(b-a+1)
    else:
        print(R1 - L1 + 1 + R2 - L2 + 1)
if __name__ == '__main__':
    main()
