sx, sy, tx, ty = map( int, input().split())
y = ty - sy
x = tx - sx
ans = "U"*y + "R"*x + "D"*y + "L"*x + "L" +  "U"*(y+1) + "R"*(x+1) + "D" + "R" + "D"*(y+1) + "L"*(x+1)+"U"
print(ans)
