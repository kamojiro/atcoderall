#import sys
#input = sys.stdin.readline
def main():
    S = input()
    T = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()








