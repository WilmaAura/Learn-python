def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
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
def calculate_slope ():
    print ("=== Calculate the slope!! ===")
    m = int(input("Input the slope (m):"))
    b = int (input("Input y-intercept:"))
    y = (0, b)
    if m != 0:
        x = (-b/m , 0)
    else:
        x = None