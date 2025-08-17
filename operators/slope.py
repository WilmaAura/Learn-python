# slope: kemiringan
print ("=== Calculate the slope!! ===")
m = int(input("Input the slope (m):"))
b = int (input("Input y-intercept:"))
y = (0, b)
if m != 0:
    x = (-b/m , 0)
else:
    x = None

print ("y intercepts: ", y)
print ("X intercepts: ", x)

