print("Please enter your times (in minutes) for each of the following events: ")
event1 = input("Swimming: ")
event2 = input("Cycling: ")
event3 = input("Running: ")

total_time = int(event1) + int(event2) + int(event3)
print("Your total time is", total_time)

qualifying_time = 100

if total_time <= qualifying_time:
    print("You will recieve the Provincial Colours Award.")

elif (total_time > 100) and (total_time <= 105):
    print("You will recieve the Provincial Half Colours Award.")

elif (total_time > 105) and (total_time <= 110):
    print("You will recieve the Provincial Scroll Award.")

elif total_time > 111:
    print("You will not recieve an award.")


