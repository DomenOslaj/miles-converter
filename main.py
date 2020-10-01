#Create a program that converts units. More specifically, kilometers into miles.

print ("Hi, i am Unit converter. Please enter a number of kilometers and i can convert it into miles.")

while True:
    km_input = input("Please enter a number of kilometers you want to convert. ")

    miles = float(km_input) * 0.621371

    print(miles)
