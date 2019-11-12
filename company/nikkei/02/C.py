#import sys
#input = sys.stdin.readline
def main():
    N = 4
    r = [i for i in range(N)]
    T = set()
    for i in range(N):
        for j in range(N):
            r[i], r[j] = r[j], r[i]
            T.add(tuple(r))
            r[i], r[j] = r[j], r[i]
    S = list(T)
    for s in S:
        s = list(s)
        for i in range(N):
            for j in range(N):
                s[i], s[j] = s[j], s[i]
                T.add(tuple(s))
                s[i], s[j] = s[j], s[i]
        
    T = list(T) 
    print(len(T))
    print(T)
if __name__ == '__main__':
    main()
