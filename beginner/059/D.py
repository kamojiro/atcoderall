#相手に差が1以下である状態を押し付け続けられるか
X, Y = map( int, input().split())
if abs( X-Y) <= 1:
    print("Brown")
else:
    print("Alice")
