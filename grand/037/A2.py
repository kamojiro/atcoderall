#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = len(S)
    now = S[0]
    comp = ""
    ans = 1
    need = 0
    for i in range(1,N):

        if need == 0:
            comp = S[i]
        else:
            comp += S[i]
            need = 0
        if now != comp:
            ans += 1
            now = comp
        else:
            need = 1
    print(ans)
if __name__ == '__main__':
    main()
