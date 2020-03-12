import sys
input = sys.stdin.readline
def main():
    N, D, K = map( int, input().split())
    LR = [ tuple( map( int, input().split())) for _ in range(D)]
    ST = [ tuple( map( int, input().split())) for _ in range(K)]
    ANS = []
    for s, t in ST:
        x, y = s, s
        for i in range(D):
            l, r = LR[i]
            if r < x or y < l:
                continue
            if l < x:
                x = l
            if y < r:
                y = r
            if  x <= t  and t <= y:
                ANS.append(i+1)
                break
    print("\n".join( map( str, ANS)))
    
if __name__ == '__main__':
    main()
