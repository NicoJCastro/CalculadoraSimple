# Este código define una clase llamada Flight que representa un vuelo con una capacidad específica.

class Flight():
    # La clase Flight tiene tres métodos:
    
    # 1__init__(self, capacity): Este es el método constructor de la clase. Se llama automáticamente cuando 
    # se crea un nuevo objeto de la clase Flight. Este método toma un argumento capacity que representa la 
    # capacidad total de pasajeros que el vuelo puede llevar. También inicializa una lista vacía self.passengers
    # que almacenará los nombres de los pasajeros.
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    # add_passenger(self, name): Este método intenta agregar un pasajero al vuelo. 
    # Primero, verifica si hay asientos disponibles llamando al método self.open_seats().
    # Si no hay asientos disponibles, el método devuelve False. Si hay asientos disponibles,
    # agrega el nombre del pasajero a la lista self.passengers y devuelve True.
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
     
    # open_seats(self): Este método devuelve el número de asientos disponibles en el vuelo. 
    # Lo hace restando el número de pasajeros actuales (la longitud de self.passengers) 
    # de la capacidad total del vuelo (self.capacity).
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    # Después de definir la clase, el código crea un nuevo objeto Flight con una capacidad de 3.
    # Luego, crea una lista de personas y trata de agregar cada persona al vuelo. Si la persona se 
    # agrega con éxito, imprime un mensaje de éxito. Si la persona no se puede agregar porque el vuelo está lleno,
    # imprime un mensaje indicando que no hay asientos disponibles.
       
flight = Flight(3)
people = ["Nico", "Anita", "Luis", "Miguel"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")