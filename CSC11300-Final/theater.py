from customer import Customer #imports classes from other files
from movie import Movie
from show import Show
from ticket import Ticket

class Theater:
  def __init__(self):
    self.movies = []
    self.shows = []
    self.customers = []
    self.total_revenue = 0

  def add_movie(self, title, rating, genre, description, duration): 
    movie = Movie(title, rating, genre, description, duration)#creates new movie
    self.movies.append(movie)#adds movie to movies[]
    return movie 

  def add_show(self, movieTitle, showtime, seatsAvailable):
    found = False
    for movie in self.movies:
      if (movieTitle == movie.title):#searches for movie
        found = True
        show = Show(movieTitle, showtime, seatsAvailable)#creates new show
        self.shows.append(show)#adds show to shows[]
        break
    if (found == False):
      print("Movie not found")

  def add_customer(self, name, age, id, tickets):
    customer = Customer(name, age, id, tickets)#creates new customer
    self.customers.append(customer)#adds customer to customers[]
    return customer 
    
  def check_movie(self, title):#simplifies way to check for movie
    for movie in self.movies:
      if movie.title == title:
        return True
    return False

  def check_show(self, title, showtime):#simplifies way to check for show
    for show in self.shows:
      if show.movie == title and show.showtime == showtime:
        return True
    return False

  def check_customer(self, id):#simplifies way to check for custoemr
    for customer in self.customers:
      if customer.id == id:
        return True
    return False
  
  def update_movie(self, title, new_title, new_rating, new_genre, new_description, new_duration):
    for movie in self.movies:
      if movie.title == title:
        movie.title = new_title
        movie.rating = new_rating
        movie.genre = new_genre
        movie.description = new_description
        movie.duration = new_duration
        print(f"Movie '{movie.title}' details successfully updated.")

  def update_show(self, title, current_showtime, new_showtime, new_seats_available):
    for movie in self.movies:
      if movie.title == title:#finds movie
        break#stops search once movie is found
    for show in self.shows:
      if show.movie == title and show.showtime == current_showtime:#finds showtime
        show.showtime = new_showtime #updates showtime
        show.seatsAvailable = new_seats_available #updates seats available
        print(f"Show for '{title}' updated successfully")      

  def update_customer(self, id, new_name, new_age):
    for customer in self.customers:
      if customer.id == id:#finds customer
        break#stops search once customer is found
    customer.name = new_name #updates customer name
    customer.age = new_age #updates customer age
    print(f"Details on customer id #{id} updated successfully.")

  def sell_tickets(self, customerId, movieTitle, showtime, numAdultTickets, numChildTickets):
    found = False
    for customer in self.customers:
      if (customer.id == customerId): #finds customer
        found = True
        break#stops search once customer is found
    if (found == False): #if customer is not found
      print("Customer not found.")
      return

    found = False
    for movie in self.movies:
      if (movie.title == movieTitle): #finds movie
        found = True
        break#stops search once customer is found
    if (found == False): #if movie is not found
      print("Movie not found.")
      return

    for show in self.shows:
      if (show.movie == movie):
        if (show.showtime == showtime): #checks for shows at selected time
          if (show.seatsAvailable < (int(numAdultTickets) + int(numChildTickets))): #checks that there are enough seats for sale
            print("Not enough available seats.")
            return
        else:
          print("No shows at that time.")
          return
    
    if movie.rating == "R" and int(customer.age) < 17: #checks age for R movies
      print("The customer is too young to watch an R rated movie.")
      return
    elif movie.rating == "PG-13" and int(customer.age) < 13: #checks age for PG-13 movies
      print("The customer is too young to watch a PG-13 rated movie.")
      return

    if (int(numAdultTickets) > 0):
      ticketType = 'Adult' 
      ticket = Ticket(customer, movie, showtime, ticketType)
      for i in range(int(numAdultTickets)): #adds each adult ticket
        customer.tickets.append(ticket) #adds to customers personal tickets
      print(f"- {str(numAdultTickets)} adult ticket(s) sold to {customer.name} for {movie.title} at {showtime} for ${str(18 * int(numAdultTickets))}") #prints adult ticket sales
      self.total_revenue += 18 * int(numAdultTickets) #adds sale to total theater revenue
      
    if (int(numChildTickets) > 0): 
      ticketType = 'Child'
      ticket = Ticket(customer, movie, showtime, ticketType)
      for i in range(int(numChildTickets)): #adds each child ticket
        customer.tickets.append(ticket) #adds to customers personal tickets
      print((f"- {str(numChildTickets)} child ticket(s) sold to {customer.name} for {movie.title} at {showtime} for ${str(13 * int(numChildTickets))}")) #prints child ticket sales
      self.total_revenue += 13 * int(numChildTickets) #adds sale to total theater revenue
    
    show.seatsAvailable -= (int(numAdultTickets) + int(numChildTickets)) #removes purchased seats from available seats
    print((f"- Total transaction cost: ${str(18 * int(numAdultTickets) + 13 * int(numChildTickets))} ")) #prints total sale
    

  def currentMovies(self):
    if (len(self.movies) == 0): #if there are no current movies
      print("There are no current movies.")
      return
    for movie in self.movies: #prints info of each movie
      print(f"Movie title: {movie.title}")
      print(f"Rating: {movie.rating}")
      print(f"Genre: {movie.genre}")
      print(f"Description: {movie.description}")
      print(f"Duration(in minutes): {movie.duration}")
      print("Showtimes:")
      for show in self.shows:
        if (show.movie == movie.title): #finds shows of current movie
          print(f"    {show.showtime} ({show.seatsAvailable} seats available)")
      print()
          
  def sellFoodOrDrink(self, item, quantity):
    #assigns price based on item and quantity purchased
    if (item == "small popcorn"):
      price = int(quantity) * 6
    elif (item == "large popcorn"):
      price = int(quantity) * 8
    elif (item == "small CocaCola" or item == "small Sprite" or item == "small Fanta"):
      price = int(quantity) * 5
    elif (item == "large CocaCola" or item == "large Sprite" or item == "large Fanta"):
      price = int(quantity) * 7
    elif (item == "Hershey's bar" or item == "Twix bar" or item == "KitKat bar"):
      price = int(quantity) * 4
    
    self.total_revenue += price #adds sale to total revenue
    print(f"{str(quantity)} {item}'s sold for a total price of ${str(price)}.") 
    
  def print_total_revenue(self):
    print(f"Total theater revenue: ${str(self.total_revenue)}")#prints total theater revenue

  def print_customer_info(self, id):
    for customer in self.customers:
      if (customer.id == id): #finds customer
        break #stops search once customer is found
    print("Customer information:")
    print(f"Name: {customer.name}")
    print(f"Age: {customer.age}")
    print(f"Customer ID: {customer.id}")
    if (len(customer.tickets) != 0): #if customer bought tickets
      print("Tickets purchased:")
      for ticket in customer.tickets: #prints info of each ticket
        print(f"- Movie: {ticket.movie.title}")
        print(f"    Showtime {ticket.showtime}")
        print(f"    Ticket Type {ticket.ticket_type}")
    else: #if customer did not buy tickets
      print("No tickets purchased by this customer yet.")