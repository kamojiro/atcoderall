#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = len(S)
    i = 0
    while i < N:
        i += 1
        if S[i-1] == 'o':
            continue
        if S[i-1] == "k":
            continue
        if S[i-1] == "u":
            continue
        if S[i-1] == "c":
            if i < N:
                if S[i] == "h":
                    i += 1
                    continue
        print("NO")
        return
    print("YES")
if __name__ == '__main__':
    main()
