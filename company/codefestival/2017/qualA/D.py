H, W, d = map( int, input().split())
cnt = 0
RY = ['R', 'Y']
GB = ['G', 'B']
now = RY
if H <= W:
    for i in range(H):
        cnt += 1
        if cnt == d:
            if now == RY:
                now = GB
            else:
                now = RY
            cnt = 0
        for j in range(i+1):
            
        
        
