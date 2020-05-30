#import sys
#input = sys.stdin.readline
def main():
    T = input()
    p = False
    ans = []
    for t in T:
        if t == "?":
            ans.append("D")
        else:
            ans.append(t)
    print("".join(ans))
if __name__ == '__main__':
    main()

