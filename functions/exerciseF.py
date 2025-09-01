def add_two_numbers (x, y):
    sum = x + y
    return sum
print(add_two_numbers(2, 3))

def area_circle(r):
    pi = 3.14
    area = pi * r **2
    return area
print(area_circle(7))

def add_all_nums (*nums):
    total = 0
    for num in nums:
        total +=num
    return total
print(add_all_nums(1,2,3))

def conv_C_to_F(cel):
    F = (cel * 1.8) + 32
    return F
celcius = float(input("Masukan suhu dalam Celcius:"))
print (conv_C_to_F(celcius))

def check_season(season):
    if season in ("september", "october", "november"):
        print("The season is Autumn")
    elif season in ("december", "januray", "february"):
        print("The season is Winter")
    elif season in ("march", "april", "may"):
        print("The season is Winter")
    else:
        print("The season is summer")
    return season
s = input('Input the month:')
print(check_season(s).lower())

def calculate_slope ():
    print ("=== Calculate the slope!! ===")
    m = int(input("Input the slope (m):"))
    b = int (input("Input y-intercept:"))
    y = (0, b)
    if m != 0:
        x = (-b/m , 0)
    else:
        x = None
print(calculate_slope())
