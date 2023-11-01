class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash_function(key)
        for i, (existing_key, existing_value) in enumerate(self.hash_table[index]):
            if existing_key == key:
                self.hash_table[index][i] = (key, value)
                return
        self.hash_table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        for existing_key, existing_value in self.hash_table[index]:
            if existing_key == key:
                return existing_value

    def remove(self, key):
        index = self._hash_function(key)
        for i, (existing_key, existing_value) in enumerate(self.hash_table[index]):
            if existing_key == key:
                del self.hash_table[index][i]
                return

    def display(self):
        return self.hash_table

class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers

def max_passengers_in_flight(flight_nodes, flight_number):
    max_passengers = 0
    max_trip_id = None

    for flight_node in flight_nodes:
        if flight_node.flight_number == flight_number and flight_node.passengers > max_passengers:
            max_passengers = flight_node.passengers
            max_trip_id = flight_node.trip_id

    return max_trip_id, max_passengers

my_hash_map = HashMap(7)
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.display()

print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

my_hash_map.remove("bbb")  
my_hash_map.display()

flight_nodes = [
    FlightNode(16, "Trip 1", 300),
    FlightNode(16, "Trip 2", 700),
    FlightNode(29, "Trip 1", 800),
    FlightNode(29, "Trip 2", 250),
    FlightNode(36, "Trip 3", 500),
    FlightNode(36, "Trip 1", 500),
    FlightNode(36, "Trip 2", 340),
    FlightNode(36, "Trip 3", 900),
    FlightNode(36, "Trip 4", 400),
    FlightNode(49, "Trip 1", 250),
    FlightNode(49, "Trip 2", 550),
]

max_passengers = max_passengers_in_flight(flight_nodes, 49)
if max_passengers is not None:
    print("Largest number of people in flight at once:", max_passengers)
else:
    print("Flight not found in the map")
