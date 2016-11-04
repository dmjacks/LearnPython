# variable car equals 100
cars = 100

# variable space_in_a_car equals 4
space_in_a_car = 4

# variable drivers equals 30
drivers = 30

# variable passengers equals 90
passengers = 90

# variable cars_not_driven equals the result of cars - drivers
cars_not_driven = cars - drivers

# variable cars_driven is equal to drivers
cars_driven = drivers

# variable carpool_capacity is equal to the product of cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# variable average_passengers_per_car is equal to the result of passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."