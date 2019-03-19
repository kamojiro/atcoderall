N = int( input())
s = N - N//60*60
N //= 60
m = N - N//60*60
N //= 60
h = N
print( str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
