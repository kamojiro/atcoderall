#import sys
#input = sys.stdin.readline
def main():
    S = [ int(x) for x in input()][::-1] + [0]
    ans = sum(S)
    t = 0
    N = len(S)-1
    cus = ans
    ten = 0
    for i in range(N):
        if i < t:
            continue
        if S[i] == 0:
            continue

        while t < N:
            if S[t] == 0:
                t += 1
                break
            if S[t+1] < 9:
                cus -= S[t]-1
                S[t+1] += 1
                ten += 10-S[t]
                S[t] = 0

                S[t+1] += 1
                t += 1
                break
            ten += 10-S[t]
            cus -= S[t]
            S[t+1] = 0
            S[t] = 0
            t += 1
#        print(i, cus, ten)
        if ten + cus < ans:
            ans = ten + cus
    print(ans)
if __name__ == '__main__':
    main()
