#Importing the necessary modules
from datetime import date, datetime
import calendar
#from datetime import datetime
#Getting user input

try: 
    last_birthday = input('Enter your last birthdate (i.e. 2017,07,01)')
    year, month, day = map(int, last_birthday.split(','))
    Age_lastbthday = int(input("Age, as at last birthday? "))

#Converting to Date object

    date_ = date(year, month, day).weekday()
    Year_born =  year - Age_lastbthday  #Year born from User Input
    born_str = str(Year_born)     #Birth year to string
    conc = (str(Year_born) + str(month) + str(day))  #Concatenation (Year_born, month and day) from date object
    born_date = datetime.strptime(conc,  '%Y%m%d')   #To get the necessary date format
    week = datetime.strptime(conc, '%Y%m%d').weekday()   #To get the actual birth day of the week
    print(f"Thank you for coming around. You were born on { born_date} which happens to be on {(calendar.day_name[week]) }")
#print( (calendar.day_name[week]) )

except:
        ValueError
        print("Wrong Input! Please make sure your input is in this format: 2017,07,01 ")
quit()

