def calcu(X, l, r, now):
    ans = 0
    for _ in range(r-l+1):
        if X[l] - now >= now + (L - X[r]):
            ans += X[l] - now
            now = X[l]
            l += 1
        else:
            ans += L - X[r] + now
            now = -L+X[r]
            r -= 1
    return ans
