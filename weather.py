print("--------------------------------------------------------------------------------")
print("        WEATHER STATS ANALYZER")
print("--------------------------------------------------------------------------------")

def highest_temperature(temp_list):
    return max(temp_list)

def lowest_temperature(temp_list):
    return min(temp_list)

def average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)

def days_above_average(temp_list, average):
    count = 0
    for temp in temp_list:
        if temp > average:
            count += 1
    return count

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

while True:

    temperatures = []
    day_temperature = []

    while True:
        try:
            days = int(input("\nEnter number of days: "))
            if days > 0:
                break
            else:
                print("Number of days should be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(days):

        while True:
            try:
                temp = float(input(f"Enter temperature for Day {i+1}: "))
                temperatures.append(temp)

                day_temperature.append((f"Day {i+1}", temp))
                break

            except ValueError:
                print("Invalid temperature. Please enter a number.")

    highest = highest_temperature(temperatures)
    lowest = lowest_temperature(temperatures)
    average = average_temperature(temperatures)
    above_avg = days_above_average(temperatures, average)

    unique_temperatures = set(temperatures)

    print("--------------------------------------------------------------------------------")
    print("WEATHER REPORT")
    print("--------------------------------------------------------------------------------")

    print("\nDaily Temperatures:")

    for day in day_temperature:
        print(f"{day[0]} : {day[1]}^C")

    print("\nHighest Temperature :", highest, "^C")
    print("Lowest Temperature  :", lowest, "^C")
    print("Average Temperature :", round(average, 2), "^C")
    print("Days Above Average  :", above_avg)

    print("\nUnique Temperatures")
    print(unique_temperatures)

    while True:
        try:
            search_temp = float(input("\nEnter temperature to search: "))

            if search_temp in unique_temperatures:
                print("Temperature was recorded.")
            else:
                print("Temperature was NOT recorded.")
            break

        except ValueError:
            print("Please enter a valid temperature.")

    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:
        choice = input("Enter your choice (1/2): ")

        if choice == "1":

            while True:
                try:
                    celsius = float(input("Enter Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"{celsius}^C = {fahrenheit:.2f}^F")
                    break
                except ValueError:
                    print("Please enter a valid number.")

            break

        elif choice == "2":

            while True:
                try:
                    fahrenheit = float(input("Enter Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"{fahrenheit}^F = {celsius:.2f}^C")
                    break
                except ValueError:
                    print("Please enter a valid number.")

            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    while True:
        continue_choice = input("\nDo you want to analyze another weather report? (Y/N): ").upper()

        if continue_choice == "Y":
            break

        elif continue_choice == "N":
            print("\nThank you for using Weather Stats Analyzer!")
            exit()

        else:
            print("Please enter Y or N.")