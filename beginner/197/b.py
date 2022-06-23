def main():
    H, W, X, Y = map(int, input().split())
    S = [ input() for _ in range(H)]
    X -= 1
    Y -= 1
    ans = 1
    for i in reversed(range(X)):
        if S[i][Y] == ".":
            ans += 1
        else:
            break
    for i in range(X+1, H):
        if S[i][Y] == ".":
            ans += 1
        else:
            break
    for j in reversed(range(Y)):
        if S[X][j] == ".":
            ans += 1
        else:
            break
    for j in range(Y+1, W):
        if S[X][j] == ".":
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()