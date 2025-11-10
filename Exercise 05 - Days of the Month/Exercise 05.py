months = { #month number: number of days
    1: 31, #number of days in January
    2: 28, #number of days in February (non-leap year)
    3: 31, #number of days in March
    4: 30, #number of days in April
    5: 31, #nummber of days in May
    6: 30, #number of days in June
    7: 31, #number of days in July
    8: 31, #number of days in August
    9: 30, #number of days in September
    10: 31, #number of days in October
    11: 30, #number of days in November
    12: 31 #number of days in December
}

month_num = int(input("enter month number: ")) #asking user for month number

if month_num in months: #checking if month number is valid
    if month_num == 2: #checking if month is February
        leap_year = input("Is it a leap year? (yes/no): ").lower() #asking user if it's a leap year
        if leap_year == "yes": #checking if it's a leap year
            print("29 days") #printing number of days in February for leap year
        else: #else for non-leap year
            print(f"{months[month_num]} days") #printing number of days in February for non-leap year
    else: #else for months other than February
        print(f"{months[month_num]} days") #printing number of days in the month
else: #else for invalid month number
    print("Invalid month number") #printing error message if month number is invalid

