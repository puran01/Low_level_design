from enum import Enum
import time

class Direction(Enum):
    UP = 1
    DOWN = 2

class Request:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
class Elevator:
    def __init__(self, id, cur_floor=0):
        self.id = id
        self.cur_floor = cur_floor
        self.direction = Direction.UP
        self.requests = []
    
    def add_requests(self,request):
        self.requests.append(request)
        print(f"Elevator {self.id} received request from {request.source} to {request.destination}.")
    
    def move(self):
        while self.requests:
            request = self.requests.pop(0)
            self._move_to_floor(request.source)
            self._move_to_floor(request.destination)
            print(f"Elevator {self.id} completed request to {request.destination}.\n")

    def _move_to_floor(self, target_floor):
        while self.cur_floor != target_floor:
            if self.cur_floor < target_floor:
                self.cur_floor += 1
                self.direction = Direction.UP
            else:
                self.cur_floor -=1
                self.direction = Direction.DOWN
            print(f"Elevator {self.id} at floor {self.cur_floor} moving {self.direction.name}")
            time.sleep(0.3)


class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators
    
    def handle_request(self,source,destination):
        nearest_elevator = None
        smallest_distance = float("inf")

        # Loop through all elevators to find the nearest one
        for elevator in self.elevators:
            distance = abs(elevator.cur_floor - source)
            if distance < smallest_distance:
                smallest_distance = distance
                nearest_elevator = elevator

        # After finding the best elevator, assign the request to it
        if nearest_elevator:
            nearest_elevator.add_requests(Request(source, destination))

class ElevatorSystem:
    def __init__(self, number_of_elevators):
        self.controller = ElevatorController([Elevator(i) for i in range(number_of_elevators)])

    def start(self):
        for elevator in self.controller.elevators:
            elevator.move()

system = ElevatorSystem(number_of_elevators=2)
controller = system.controller

# Simulate user requests
controller.handle_request(0, 12)
controller.handle_request(3, 8)
controller.handle_request(2, 0)

# Start elevators
system.start()
             