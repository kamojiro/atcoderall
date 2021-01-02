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
        f = [200]*L
        p = 0
        for i, s in enumerate(S):
            if s == b:
                f[i] = min(f[i],i-p)
                p = i+1
            if s == b and i > 0 and i < L-1:
                if S[i-1] == a and S[i+1] == a:
                    check = True
        if not check:
            break

        p = L-1
        # print(f)
        g = [200]*L
        for i, s in enumerate(S[::-1]):
            i = L-1-i
            if s == b:
                g[i] = min(g[i], p-i)
                p = i-1
        
        fg = [(min(f[i], g[i]), -max(f[i], g[i]),i) for i in range(L)]
        fg.sort()
        for i in range(L):
            if fg[i][0] >= 1:
                _, _,i = fg[i]
                break
        S = S[:i-1] + S[i+1:]
        L -= 1
        count += 1
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
