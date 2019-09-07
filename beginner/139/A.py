#import sys
#input = sys.stdin.readline
def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()








