N = int( input())
anseven = 0
for i in range(1,N//2):
    anseven += int(N/2+i) - int(N/2-i-0.1)-1
if N%2 == 1:
    print(anseven*2+N-2)
else:
    print(anseven*2)
        
