N=int(input())
W=[tuple(input().split()) for _ in range(N)]
U=[]
R=[]
D=[]
L=[]
for x,y,u in W:
 x,y = int(x),int(y)
 if u=="U":
  U.append((x,y))
 elif u=="D":
  D.append((x,y))
 elif u=="L":
  L.append((x,y))
 else:
  R.append((x,y))
r=10**9
def z(A):
 global r
 A.sort()
 n=p=-10**9
 for k,c,a in A:
  if k!=n:
   if a==1:
    n=k
    p=c
   continue
  if a==1:
   p=c
   continue
  if (c-p)*5<r:
   r=(c-p)*5
z([(x,y,1) for x,y in U]+[(x,y,-1) for x,y in D])
z([(y,x,1) for x,y in R]+[(y,x,-1) for x,y in L])
z([(x+y,x-y,1) for x,y in R]+[(x+y,x-y,-1) for x,y in U])
z([(x+y,x-y,1) for x,y in D]+[(x+y,x-y,-1) for x,y in L])
z([(x-y,x+y,1) for x,y in U]+[(x-y,x+y,-1) for x,y in L])
z([(x-y,x+y,1) for x,y in R]+[(x-y,x+y,-1) for x,y in D])
print("SAFE" if r>=10**9 else r)
