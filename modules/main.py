# Importing module
import mymodule
print(mymodule.generate_full_name('Wilma', 'Auraruna Khalif'))

# import all the functions differentl  
from mymodule import generate_full_name as fullname, check_season as season, calculate_slope as slope
print(fullname('Wilma', 'Auraruna Khali'))
print (season('september'))

