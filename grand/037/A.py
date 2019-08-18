#import sys
#input = sys.stdin.readline
def main():
    S = input()
    N = int( len(S))
    now = S[0]
    ANS = [1]
    for i in range(1,N):
        if now == S[i]:
            ANS[-1] += 1
        else:
            ANS.append(1)
            now = S[i]
    ans = 0
    for a in ANS:
        if a%3 == 0:
            ans += a//3*2
        else:
            ans += a//3*2+1
    print(ans)
if __name__ == '__main__':
    main()
