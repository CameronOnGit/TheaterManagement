def forceInt(variable): #Forces the user to input an integer for variables that are integer types (ID, price, quantity). Otherwise the program would crash when it tries to perform math operations on string inputs.
  while(True):
      userInput = (input('Enter ' + variable + ":"))
      try:
        int(userInput)
        break
      except:
        print("The " + variable + " must be a number. (Example: '4'")
        continue

  return userInput


def forceTime():
  while (True):
    print("Please input a number from 1-12 for the hour of the show.")
    hour = int(forceInt("hour")) #Forces hour time in loop
    if (hour >= 1 and hour <= 12): 
      break
    else:
      print("That is an invalid input. Please try again.")
      
  while (True):    
    print("Please input a number from 0-59 for the minute of the show.")
    minute = int(forceInt("minute")) #Forces minute time in loop
    if (minute >= 0 and minute <= 59):
      break
    else:
        print("That is an invalid input. Please try again.")
      
  while(True):    
    print("Please input either 'AM' or 'PM' to indicate the time of the show:")
    ampm = input("Time:").upper() #To upper to handle case sensitivity
    if (ampm == 'AM' or ampm == 'PM'):
      break
    else:
        print("That is an invalid input. Please try again.")

  if (minute < 10): #For 01-09 minutes times
    showtime = f"{str(hour)}:0{minute} {ampm} "

  else:
    showtime = f"{str(hour)}:{minute} {ampm} "
    

  return showtime
  