#import sys
#input = sys.stdin.readline
def greed(S, T):
    check = True
    L = len(S)
    count = 0
    while check and L >= 3:
        check = False
        for i in range(len(S)-2):
            if S[i:i+3] == T:
                count += 1
                S = S[:i] + S[i+3:]
                check = True
                L -= 3
    return count

def solve(S,T):
    check = True
    L = len(S)
    count = 0
    a = T[0]
    b = T[1]
    while check and L >= 3:
        check = False
        f = [0]*L
        p = 0
        for i, s in enumerate(S):
            if s == a:
                p += 1
            elif s == b:
                f[i] += p
                p = 0
            else:
                p = 0
        p = 0
        # print(f)
        for i, s in enumerate(S[::-1]):
            i = L-1-i
            if s == a:
                p += 1
            elif s == b:
                f[i] += p
                p = 0
            else:
                p = 0
        # print(f)
        m = 0
        for i, s in enumerate(S):
            if i == 0 or i == L-1:
                continue
            if s == b:
                if S[i-1] == a and S[i+1] == a:
                    if m < f[i]:
                        m = f[i]
        # print(S,m)
        for i, s in enumerate(S):
            if i == 0 or i >= L-1:
                continue
            if s == b:
                # print(S,i)
                if S[i-1] == a and S[i+1] == a:
                    if f[i] == m:
                        S = S[:i-1] + S[i+2:]
                        count += 1
                        L -= 3
                        check = True
    return count
    
    
def main():
    N = int( input())
    S = list( input())
    T = list( input())
    if T[0] == T[2] and T[0] != T[1]:
        print(solve(S,T))
    else:
        print(greed(S,T))
    
if __name__ == '__main__':
    main()
