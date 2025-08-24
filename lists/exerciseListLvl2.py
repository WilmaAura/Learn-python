ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age= min(ages)
max_age=max(ages)
print(min_age)
print(max_age)

n = len(ages)//2
median = (ages[n] + ages[n-1])/2
print (median)

# find the average age
average = sum(ages)/len(ages)
print ("Average:",average)

# find the range of the ages 
range = max_age - min_age
print ("range:", range)

# compare the value of (min - average) and (max - average)
# use abs() method
# abs (): meaning absolute value of a number. It can't be negative
value1 = min_age - average
print(abs(round(value1, 2)))
value2 = max_age - average
print(abs(round(value2, 2)))



