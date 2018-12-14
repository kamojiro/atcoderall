# Counterをとって、2つ以上あるものが2つ以上あるものがいくつあるかをまず調べる。
# そのあと、それらを大きい順に並べて、順番に引き算をおこなっていけば解決するはず
# それだけじゃ足りなくて、例えば同じ数が2つ以上あれば同じ数を3つ選んで減らすことができる。
# 今回は引き算を先にやったけど、減らすのを先にやってもいいかも？ほんまか？
from collections import Counter
N = int( input())
A = list( map( int, input().split()))
CA = Counter(A)
V = []
for x in CA:
    if CA[x] >= 2:
        V.append(CA[x]-1)
V.sort(key = None, reverse = True)
now = 0
ans = 0
for v in V:
    ans += v
    if now <= 0:
        now += v
    else:
        now -= v
b = abs(now)
if b%2 == 1:
    ans += 1
print( max(0,N-ans))
