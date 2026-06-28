#take input
year = int(input("enter the year:"))

#logic
if year%4 == 0:
    print("this is a leap year")
elif year%400 ==0 :
    print("this is a leap year")
else :
    print("this is not a leap year")
