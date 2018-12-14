Q = int( input())
for _ in range(Q):
    A, B, C = map( int, input().split())
    if A%2 == 0:
        if B%2 == 0:
            if C%2 == 0:
                ans = 'Yes'
            else:
                ans = 'No'
        else:
            if C>= 10 and C%2 == 0:
                ans = 'Yes'
            else:
                ans = 'No'
    else:
        if B*10 + C >= 100:
            if B*10 >= 100:
                B -= 10
                if B%2 == 0:
                    if C%2 == 0:
                        ans = 'Yes'
                    else:
                        ans = 'No'
                else:
                    if C>= 10 and C%2 == 0:
                        ans = 'Yes'
                    else:
                        ans = 'No'
            else:
                if C >= (10-B)*10 and C%2 == 0:
                    ans = 'Yes'
                else:
                    ans = 'No'
                    
        else:
            ans = 'No'
    print(ans)
