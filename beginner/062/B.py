H, W = map( int, input().split())
P = [ input() for _ in range(H)]
print('#'*(W+2))
for i in range(H):
    print('#'+P[i]+'#')
print('#'*(W+2))

