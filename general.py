# ternary if

number = 10

if number > 0:
    print("positive")
else:
    print("0 or negative")

# the same as:
message = "positive" if number > 0 else "0 or negative"
print(message)

# or:
print("positive" if number > 0 else "0 or negative")


names = ["Jacob", "Gabrielle", "Genevieve", "Lucas"]

# for loops
for name in names:
    print(name.upper())

# loop through dictionaries
person = {
    "name": "Jamal",
    "age": 23,
    "address": "Sezamkowa 420"
}

for key in person:
    print(f"key: {key}, value: {person[key]}")

for key, value in person.items():
    print(f"key: {key}, value: {value}")

# while loop
number = 0

while number < 5:
    number += 2
    print(number)
else:
    print("While loop ended")