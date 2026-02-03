class Vehicle:
  def __init__(self, vehicle_id,brand,rent_per_day):
    self.vehicle_id = vehicle_id
    self.brand = brand
    self.rent_per_day = rent_per_day

  def display_details(self):
    print("Vehicle ID: ", self.vehicle_id)
    print("Brand: ", self.brand)
    print("Rent per day: ", self.rent_per_day)

  def calculate_rent(self, days):
    return self.rent_per_day * days

V1 = Vehicle(101, "Kia", 5000)
V2 = Vehicle(202, "Toyota", 6000)

V1.display_details()
print("Rent for 5 days:", V1.calculate_rent(5))

V2.display_details()
print("Rent for 3 days:", V2.calculate_rent(3))
