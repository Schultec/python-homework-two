while True:
#take input between 1 and 7
    dow = int(input("enter a number between one and seven to represent the day of the week:"))
#find day of week
    if dow == 5:
        print("today is friday")
        break
    elif dow == 4:
        print("today is thursday")
        break
    elif dow == 3:
        print("today is wednesday")
        break
    elif dow == 2:
        print("today is tuesday")
        break
    elif dow == 1:
        print("today is monday")
        break
#add happy weekend if chosen number is 6 or 7
    elif dow == 6:
        print("today is saturday")
        print("happy weekend")
        break
    elif dow == 7:
        print("today is sunday")
        print("happy weekend")
        break
#error if number is to large and loop to start
    else:
        print("please try again")
        
        
   
