import sys, random, math, datetime, calendar, os, antigravity

#print pythonpath
print("1. Print python path env: ", sys.path)

#print a random integer between 1 and 10
print("2. Print random num from 1 - 10: ", random.randint(1, 10))

#print a random number from a list
my_list = [1, 2, 3, 4, 5]
print("3. Print random number from my_list", my_list,": ", random.choice(my_list))

#Import math lib as shown above, print the square root of 16   
print("4. Print square root of 16: ", math.sqrt(16))
#Print radian of 90 degrees
print("5. Print radian of 90 degrees: ", math.radians(90))
#Print the sine value of 90 degrees
print("6. Print sine of 90 degrees: ", math.sin(math.radians(90)))  

#Print date and time now
print("7. Print date and time now: ", datetime.datetime.now())
print("7. Print date and time today: ", datetime.datetime.today())

#Print calendar for a given year and month
print("8. Print calendar for 2026 and 8: ", calendar.month(2026, 8))
#print("8. Print calendar for 2026: ", calendar.calendar(2026))
print("8. Is 2028 is a leap year? ", calendar.isleap(2028))

#Print current working directory
print("9. Print current working directory: ", os.getcwd())  