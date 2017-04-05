# number of cars
cars = 100
# number of seats in a car (excluding the driver's seat)
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# empty cars
cars_not_driven = cars - drivers
# every driver can only drive one car, so cars_driven is equal to drivers
cars_driven = drivers
# total number of passenger seats in carpool
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers per car today
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
