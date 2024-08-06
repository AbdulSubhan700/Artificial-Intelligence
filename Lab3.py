def right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

right_angled_triangle(5)

def right_angled_triangle(n):
    for i in range(3, n + 2):
        print('*' * i)

right_angled_triangle(7)

# Define the range
start = 1500
end = 2700

# Initialize an empty list to store the results
result = []

# Loop through the range
for number in range(start, end + 1):
    # Check if the number is divisible by 7 and multiple of 5
    if number % 7 == 0 and number % 5 == 0:
        result.append(number)

# Print the results
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700:")
print(result)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    print("Temperature Conversion")
    choice = input("Choose conversion: \n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

