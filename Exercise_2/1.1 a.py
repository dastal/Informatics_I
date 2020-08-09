temperature = int(input("What is the temperature (in °C)? "))
print(temperature)

if temperature < 0:
    print("It's freezing!")
elif (temperature >= 0) and (temperature <= 20):
    print("It's mild!")
else:
    print("It's warm!")