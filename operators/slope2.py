# slope is (m=y2-y1/x2-x1)
# find the slope and Euclidean distance 
# between point (2,2) and point (6,10)

x1 = y1 = 2
x2 = 6
y2 = 10
m = (y2-y1)/(x2-x1)
print ("Slope (m):", round(m,2)) # keep only 2 decimal places

# Euclidean distance
# d(p,q) = ((p1 - q1)**2 + (p2-q2)**2)**1/2
print ("\n--- The Euclidean distance ---")
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
print ("Euclidean:", round(d,2))












