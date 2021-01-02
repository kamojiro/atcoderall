#import sys
#input = sys.stdin.readline
def main():
    S = list( input())
    X = int( input())
    before = 0
    now = 0
    T = []
    for s in S:
        T.append(s)
        before = now
        if s.isalpha():
            now += 1
        else:
            now *= (1+int(s))
        if now >= X:
            break
    G = T[::-1]
    # print(G)
    for s in G:
        if s.isalpha():
            if now == X:
                print(s)
                return
            now -= 1
            continue
        t = int(s)
        now //= (t+1)
        X = (X-1)%now+1
        # print(now, X)
    
    
    
        
if __name__ == '__main__':
    main()
