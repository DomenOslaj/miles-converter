#Create a program that converts units. More specifically, kilometers into miles.

print ("Hi, i am Unit converter. Please enter a number of kilometers and i can convert it into miles.")

while True:
    km_input = input("Please enter a number of kilometers you want to convert: ")

    miles = float(km_input) * 0.621371

    miles_short = "{:.2f}".format(miles)

    print("{0} kilometers is {1} miles." .format(km_input, miles_short))

    question = input("Would you like to convert one more number? y/n ")

    if question.lower == "n" or question.lower == "no":
        print("Thanks for using our converter!")
        break
