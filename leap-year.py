year = int(input("Enter year to be checked:"))

if(year%4==0 and year%100!=0):
    print("The year is a leap year!")
elif(year%400==0):
    print("The year is a leap year!")    
else:
    print("The year isn't a leap year!")