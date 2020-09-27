def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = 1000
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if S[i+j] != T[j]:
                cnt += 1
        if cnt < ans:
            ans = cnt
    print(ans)
if __name__ == '__main__':
    main()
