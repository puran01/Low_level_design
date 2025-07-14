class Flight:
    def __init__(self, flightno, capacity, source, destination):
        self.flightno = flightno
        self.capacity = capacity
        self.source = source
        self.destination = destination    
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.capacity:
            self.booked_seats += 1
            return True
        return False
    
    def seat_availability(self):
        return self.capacity - self.booked_seats
    
class Passenger:
    def __init__(self,name, id):
        self.name = name
        self.id = id
        self.bookings = []
    
    def check_bookings(self):
        return self.bookings

class FlightSystem:
    def __init__(self):
        self.bookings = {}
        self.flights = {}
        self.booking_counter = 1

    def add_flight(self, flight):
        self.flights[flight.flightno] = flight

    def search_flights(self,source, destination):
        res = []
        for f in self.flights.values():
            if f.source == source and f.destination == destination:
                res.append(f)    
        return res

    def book_flight(self, passenger, flight_number):
        flight = self.flights[flight_number]
        if flight and flight.book_seat():
            booking_id = self.booking_counter
            booking = Booking(booking_id,passenger,flight)
            self.bookings[booking_id] = booking
            passenger.bookings.append(booking)
            self.booking_counter += 1
            return booking
        return None
class Booking:
    def __init__(self, booking_id, passenger, flight):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.status = "Confirmed"


system = FlightSystem()


flight1 = Flight("AI101", 20, "NYC", "LAX")
flight2 = Flight("AI102", 200, "NYC", "LAX")
flight3 = Flight("AI103", 150, "NYC", "SFO")

system.add_flight(flight1)
system.add_flight(flight2)
system.add_flight(flight3)

print("Flights from NYC to LAX:")
flights_to_lax = system.search_flights("NYC", "LAX")
for flight in flights_to_lax:
    print(f"Flight: {flight.flightno}, Seats Available: {flight.seat_availability()}")

passenger = Passenger("John Doe", 1)

booking = system.book_flight(passenger, "AI101")
if booking:
    print(f"\nBooking Confirmed: Booking ID {booking.booking_id}, Flight {booking.flight.flightno}")
else:
    print("\nBooking Failed: No seats available.")

# Show passenger bookings
print("\nPassenger's Bookings:")
for b in passenger.check_bookings():
    print(f"Booking ID: {b.booking_id}, Flight: {b.flight.flightno}, Status: {b.status}")

# Check flight seat availability again after booking
print(f"\nSeats available in AI101 after booking: {flight1.seat_availability()}")
