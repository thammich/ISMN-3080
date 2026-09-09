# Practice 1
name = "Sam"
age = 20
favColor = "Blue"

print(name)
print(age)
print(favColor)

# Practice 2
first_name = "Sam"
last_name = "Lin"
city = "Auburn"
state = "Alabama"

print(f"{first_name} {last_name} lives in {city}, {state}")

# Practice 3
product = "apples"
price = 1.50
quantity = 3

print(f"I bought {quantity} {product} at ${price:.2f} each.")

# Practice 4
num1 = "300"
num2 = "250"

print(int(num1) + int(num2))

# Practice 5
age = 20

if (age >= 18):
    print("You are an adult")

# Practice 6
score = 70

if (score >= 70):
    print("You passed!")

# Practice 7
money = 19.99

if (money >= 20):
    print("You can buy it.")
else:
    print("You cannot buy it")

# Practice 8
temperature = 0

if (temperature < 50):
    print("Cold")
elif (temperature >= 50 and temperature <= 79):
    print("Warm")
elif (temperature >= 80):
    print("Hot")