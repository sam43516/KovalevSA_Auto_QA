def is_year_leap(year):
    if year % 4 == 0:
        x ="год " + str(year) +": " + str(True)
        print(x)
    else:
        x ="год " + str(year) +": " + str(False)
        print(x)

is_year_leap(2216)  
