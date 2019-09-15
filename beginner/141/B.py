#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = len(S)
    for i in range(0, N, 2):
        if S[i] == "L":
            print("No")
            return
    for i in range(1,N,2):
        if S[i] == "R":
            print("No")
            return
    print("Yes")
if __name__ == '__main__':
    main()
