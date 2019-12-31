#import sys
#input = sys.stdin.readline

def main():
    H, W = map( int, input().split())
    S = [ input() for _ in range(H)]
    def check_color(s, t, color):
        if not (0 <= s <= H-1 and 0 <= t <= W-1):
            return False
        for i in range(-1,2):
            for j in range(-1,2):
                if 0 <= s+i <= H-1 and 0 <= t+j <= W-1:
                    if S[s+i][t+j] != color:
                        return False
        return True
    ans = True
    for a in range(H):
        for b in range(W):
            if S[a][b] == '.':
                continue
            check = False
            for x in range(-1,2):
                for y in range(-1,2):
                    if check_color(a+x, b+y,'#'):
                        check = True
                        break
                if check:
                    break
            if not check:
                ans = False
    if not ans:
        print("impossible")
        return
    else:
        print("possible")
    ans = [[] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if check_color(i, j, '#'):
                ans[i].append('#')
            else:
                ans[i].append('.')
    for i in range(H):
        print("".join(ans[i]))
    
                
if __name__ == '__main__':
    main()
