#import sys
#input = sys.stdin.readline
def main():
    H, W = map( int, input().split())
    ans = min(H,W)
    if H%3 == 0 or W%3 == 0:
        ans = 0
    for i in range(1,H):
        L = [W*i]
        L.append(W//2*(H-i))
        if W%2 == 1:
            L.append((W//2+1)*(H-i))
        if max(L) - min(L) < ans:
            ans = max(L) - min(L)
    for i in range(1,W):
        L = [H*i]
        L.append(H//2*(W-i))
        if H%2 == 1:
            L.append((H//2+1)*(W-i))
        if max(L) - min(L) < ans:
            ans = max(L) - min(L)
    print(ans)
if __name__ == '__main__':
    main()
