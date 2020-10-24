#import sys
#input = sys.stdin.readline
def solve():
    N = int(input())
    A = list(map(int,input().split()))
    if N == 1:
        return "Second"
    if N == 2:
        if A[0]^A[1] == 0:
            return "Second"
        else:
            return "First"
    if N%2 == 0:
        return "Second"
    else:
        return "First"
        
    

def main():
    T = int(input())
    ANS = [solve() for _ in range(T)]
    print("\n".join(ANS))
    

if __name__ == '__main__':
    main()
