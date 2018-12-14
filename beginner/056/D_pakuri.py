N, K = map( int, input().split())
A = list( map( int, input().split()))
RA = sorted(A)
RA = RA[::-1]
s = 0
ans = 0
for i in range(N):
    a = RA[i]
    if s+a < K:
        s += a
        ans += 1
    else:
        ans = 0
print(ans)
#反例
#5 12
#6 4 3 2 1
#通るらしいけどなんでかわからない
#https://beta.atcoder.jp/contests/abc056/submissions/2203497
    # Aのうち要素が大きいものから見ていったとき、
    # その要素を入れても総和がK未満のものだけ加えていく
    # 最後に連続して加えた要素の個数が解となる
    # (それら以外の要素の組み合わせでK以上にでき、かつ、
    #  それらの総和がK未満になるため)
