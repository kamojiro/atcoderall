from math import ceil
N = int( input())
bridge, blue = map( int, input().split())
print( bridge, blue)
for _ in range(N-1):
    t, a = map( int, input().split())
    if bridge < t and blue < a:
        bridge = t
        blue = a
    elif (bridge//t+ceil(bridge%t))*a < blue:
        blue = (blue//a+ceil(blue%a))*a
        bridge = (blue//a+ceil(blue%a))*t
    elif (blue//a+ceil(blue%a))*t < bridge:
        bridge = (bridge//t+ceil(bridge%t))*t
        blue =  (bridge//t+ceil(bridge%t))*a
    else:
        if (blue//a+ceil(blue%a))*a + (blue//a+ceil(blue%a))*t <= (bridge//t+ceil(bridge%t))*t +(bridge//t+ceil(bridge%t))*a:
            blue = (blue//a+ceil(blue%a))*a
            bridge = (blue//a+ceil(blue%a))*t
        else:
            bridge = (bridge//t+ceil(bridge%t))*t
            blue =  (bridge//t+ceil(bridge%t))*a

    print( bridge, blue)
print( bridge + blue)
