
class Customer:
  def __init__(self, name, age, id, tickets = None):
    self.name = name
    self.age = age
    self.id = id
    self.tickets = tickets if tickets is not None else [] #No tickets upon initialization. After a ticket is purchased, it is appended into the list
