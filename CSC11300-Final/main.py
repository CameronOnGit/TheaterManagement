
from theater import Theater #Accesses the other classes and functions
from errors import forceInt
from errors import forceTime

theater = Theater()


while (True): #Starts the program loop
  print("----------------------------------------------------------")
  print("Please select an option from the following choices: ")
  print("1. Add a new movie.")
  print("2. Add a new showing.")
  print("3. Add a new customer.")
  print("4. Sell a ticket.")
  print("5. View current movies and showtimes.")
  print("6. Sell food or drink.")
  print("7. Update movie details.")
  print("8. Update show details.")
  print("9. Update customer details.")
  print("10. View theater revenue.")
  print("11. View customer details.")
  print("12. Stop the program.")
  print("----------------------------------------------------------")

  userIn = input('Input:') #Gets input for user-friendly interface

  if (userIn == '1'):
    print("You have selected option 1. Add a new movie.")
    
    title = input("Enter movie title:").title()

    while(True):
      print("Select rating:")
      print("1. G")
      print("2. PG")
      print("3. PG-13")
      print("4. R")
      userInput = forceInt("input") #First instance of forceInt
      if (userInput == '1'):
        rating = "G"
        break
      elif (userInput == '2'):
        rating = "PG"
        break
      elif (userInput == '3'):
        rating = "PG-13"
        break
      elif (userInput == '4'):
        rating = "R"
        break
      else:
        print("That is an invalid input. Please try again.")
      
    genre = input("Enter movie genre:")  
    description = input("Enter description:")
    duration = forceInt("duration (minutes)")
    theater.add_movie(title, rating, genre, description, duration) #The function that adds/appends the movie

  elif (userIn == '2'):
    print("You have selected option 2. Add a new showing.")
    print("Current movies: ")
    for movie in theater.movies: #Prints all current movies first
      print(movie.title)
    movieTitle = input("Enter movie title:").title()
    if theater.check_movie(movieTitle) == False: #checks existence of the movie
      print("Movie not found.")
    else:
      for movie in theater.movies:
        if (movieTitle == movie.title):
          showtime = forceTime() #first intance of forceTime
          seatsAvailable = forceInt("available seats")
          theater.add_show(movieTitle, showtime, seatsAvailable) #Adds/appends show
          break 

  elif (userIn == '3'):
    print("You have selected option 3. Add a new customer.")
    name = input("Enter customer name:").title() #title?
    age = forceInt("customer age") 
    id = forceInt("customer ID")
    
    theater.add_customer(name, age, id, None) #Adds/appends customer. None variable since no tickets have been purchased yet.

  elif (userIn == '4'):
    print("You have selected option 4. Sell a ticket.")
    
    customerId = forceInt("customer ID") 
    if theater.check_customer(customerId) == False: #customer existence check
      print("Customer not found.")
    else:
      print("Current movies: ") #Print movies
      for movie in theater.movies:
        print(movie.title)
      movieTitle = input("Enter movie title:").title()
      
      print("Available showtimes: ") #Print showtimes of movie
      for show in theater.shows:
        if (show.movie == movieTitle and int(show.seatsAvailable) > 0):
          print(f"There are {str(show.seatsAvailable)} seats available for the {show.showtime} show.")
      
      showtime = forceTime()
      if theater.check_show(movieTitle, showtime) == False: #Check show existence
        print("No matching shows found.")
      else:
        print("How many adult tickets would the customer like?")
        numAdultTickets = forceInt("adult tickets")
        print("How many child tickets would the customer like?")
        numChildTickets = forceInt("child tickets")
        if (show.seatsAvailable < (int(numAdultTickets) + int(numChildTickets))):
            print("Not enough available seats.")
        else:
          theater.sell_tickets(customerId, movieTitle, showtime, numAdultTickets, numChildTickets)

  elif (userIn == '5'): #Self-explanatory
    print("You have selected option 5. View current movies and showtimes.")
    theater.currentMovies()

  elif(userIn == '6'): #Direct. Uses interface to select options
    print("You have selected option 6. Sell food or drink.")
    
    while(True): 
      print("Select what the customer would like to purchase:")
      print("1. Popcorn")
      print("2. Soda")
      print("3. Candy")
      userInput = forceInt("input")
      if (userInput == '1'):
        item = "popcorn"
        break
      elif (userInput == '2'):
        item = "soda"
        break
      elif (userInput == '3'):
        item = "candy"
        break
      else:
        print("That is an invalid input. Please try again.")

    if (item == 'popcorn'):
      while(True):
        print("Select what size the customer would like to purchase:")
        print("1. Small")
        print("2. Large")
        userInput = forceInt("input")
        if (userInput == '1'):
          item = "small popcorn"
          break
        elif (userInput == '2'):
          item = "large popcorn"
          break
        else:
          print("That is an invalid input. Please try again.")
          
    if (item == 'soda'):
      while(True):
        print("Select which soda the customer would like to purchase:")
        print("1. CocaCola")
        print("2. Sprite")
        print("3. Fanta")
        userInput = forceInt("input")
        if (userInput == '1'):
          sodaType = "CocaCola"
          break
        elif (userInput == '2'):
          sodaType = "Sprite"
          break
        elif (userInput == '3'):
          sodaType = "Fanta"
          break
        else:
          print("That is an invalid input. Please try again.")
      while(True):
        print("Select what size the customer would like to purchase:")
        print("1. Small")
        print("2. Large")
        userInput = forceInt("input")
        if (userInput == '1'):
          item = f"small {sodaType}"
          break
        elif (userInput == '2'):
          item = f"large {sodaType}"
          break
        else:
          print("That is an invalid input. Please try again.")

    if (item == 'candy'):
      while(True):
        print("Select which candy the customer would like to purchase:")
        print("1. Hershey's bar")
        print("2. Twix bar")
        print("3. KitKat bar")
        userInput = forceInt("input")
        if (userInput == '1'):
          item = "Hershey's bar"
          break
        elif (userInput == '2'):
          item = "Twix bar"
          break
        elif (userInput == '3'):
          item = "KitKat bar"
          break
        else:
          print("That is an invalid input. Please try again.")

    print(f"Please enter how many {item}'s the customer would like to purchase:")
    quantity = forceInt("quantity")
    
    theater.sellFoodOrDrink(item, quantity) #Calls the function

  elif (userIn == '7'):
    print("You have selected option 7. Update movie details.")
    print("Current movies: ") #Print movies
    for movie in theater.movies:
      print(movie.title)
    title = input("Enter the title of the movie you want to edit:").title()
    if theater.check_movie(title) == False: #check existence
      print("Movie not found.")
    else:
      old_title = title
      new_title = input("Enter the new title:").title() #Similar to add show
      for show in theater.shows:
        if (show.movie == old_title): #finds shows of current movie
          show.movie = new_title
      while(True):
        print("Select rating:")
        print("1. G")
        print("2. PG")
        print("3. PG-13")
        print("4. R")
        userInput = forceInt("input")
        if (userInput == '1'):
          new_rating = "G"
          break
        elif (userInput == '2'):
          new_rating = "PG"
          break
        elif (userInput == '3'):
          new_rating = "PG-13"
          break
        elif (userInput == '4'):
          new_rating = "R"
          break
        else:
          print("That is an invalid input. Please try again.")
      new_genre = input("Enter new genre:")
      new_description = input("Enter new description:")
      new_duration = forceInt("duration (in minutes)")
      theater.update_movie(title, new_title, new_rating, new_genre, new_description, new_duration) #update function
  
  elif (userIn == '8'):
    print("You have selected option 8. Update show details.")
    print("Current movies: ") #Print movies
    for movie in theater.movies:
      print(movie.title)
    title = input("Enter movie title whose showing you wish to edit:").title()
    if theater.check_movie(title) == False: #checks existence of the movie
      print("Movie not found.")
    else:
      print("Showtimes:")
      for show in theater.shows:
        if (show.movie == title): #finds shows of current movie
          print(f"    {show.showtime} ({show.seatsAvailable} seats available)")
      print()
      print("Enter the showtime of the showing you want to edit.")
      current_showtime = forceTime()
      if theater.check_show(title, current_showtime) == False: #check show's existence
        print("No matching shows found.")
      else:
        print("Enter the new information for the show.")
        new_showtime = forceTime()
        new_seats_available = forceInt("new # of available seats")
        theater.update_show(title, current_showtime, new_showtime, new_seats_available) #update function

  elif (userIn == '9'):
    print("You have selected option 9. Update customer details.")
    id = forceInt("customer ID")
    if theater.check_customer(id) == False: #check existence
      print("Customer not found.")
    else:
      new_name = input("Enter the (new) customer name:")
      new_age =  forceInt("(new) customer age")
      theater.update_customer(id, new_name, new_age) #update function

  elif (userIn == '10'): #self-explanatory 
    print("You have selected option 10. View theater revenue.")
    theater.print_total_revenue()

  elif (userIn == '11'):
    print("You have selected option 11. View customer details.")
    id = forceInt("customer ID")
    if theater.check_customer(id) == False: #checks existence
      print("Customer not found.")
    else:
      theater.print_customer_info(id)

  elif (userIn == '12'):
    print("Program stopped.")
    break
    
  else:
    print("That is an invalid input. Please try again.")

  
  