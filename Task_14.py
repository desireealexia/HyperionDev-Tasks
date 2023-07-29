# calculate holiday cost using information about hotel cost, plane cost and car rental cost

# define plane cost
def plane_cost(city_flight):
    if city_flight == 'tokyo':
        return 868
    elif city_flight == 'paris':
        return 153
    elif city_flight == 'chicago':
        return 559
    elif city_flight == 'istanbul':
        return 276
    else:
        return 0

# define hotel cost
def hotel_cost(num_nights):
    pricepernight = 100
    return num_nights * pricepernight

# define car rental cost
def car_rental(rental_days):
    costperday = 45
    return costperday * rental_days

# define holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    hotelcost = hotel_cost(num_nights)
    planecost = plane_cost(city_flight)
    carrental = car_rental(rental_days)
    total_cost = hotelcost + planecost + carrental
    return total_cost

# user inputs information
print("Below is a list of cities you can travel to:\n- Tokyo\n- Paris\n- Chicago\n- Istanbul\n")
city_flight = input("Enter the city you want to fly to: ").lower()

num_nights = int(input("How many nights will you stay at the hotel? "))
rental_days = int(input("How many days will you rent a car? "))

# prints all details about the holiday
print(f"Hotel for {num_nights} nights will cost you £{hotel_cost(num_nights)}.")
print(f"Car rental for {rental_days} days will cost you £{car_rental(rental_days)}.")
print(f"This holiday to {city_flight} will cost you £{holiday_cost(num_nights, city_flight, rental_days)}")
