H, W = map( int, input().split())
if H%3 == 0 or W%3 == 0:
    ans = 0
else:
    ans = min( max((H//3+1)*W, (H//3)*W)- min((H//3+1)*W, (H//3)*W),  max((W//3+1)*H, (W//3)*H)- min((W//3+1)*H, (W//3)*H))
    for i in range(H+1):
        ans = min( ans, max(W*i, (H-i)*(W//2), (H-i)*(W - W//2)) - min(W*i, (H-i)*(W//2), (H-i)*(W - W//2)))
    for j in range(W+1):
        ans = min( ans, max(H*j, (W-j)*(H//2), (W-j)*(H - H//2)) - min(H*j, (W-j)*(H//2), (W-j)*(H - H//2)))
print(ans)
