#import sys
#input = sys.stdin.readline
def main():
    N = 10
    CAA, CAB, CBA, CBB = list(input())
    S = set(["AB"])
    for i in range(2,N):
        T = set()
        for s in S:
            for j in range(i-1):
                if s[j] == "A" and s[j+1] == "A":
                    T.add(s[:j+1] + CAA + s[j+1:])
                elif s[j] == "A" and s[j+1] == "B":
                    T.add(s[:j+1] + CAB + s[j+1:])
                elif s[j] == "B" and s[j+1] == "A":
                    T.add(s[:j+1] + CBA + s[j+1:])
                else:
                    T.add(s[:j+1] + CBB + s[j+1:])
        S = T
        print(i+1, len(S), S)
            
if __name__ == '__main__':
    main()
