# some some usefull methods
numbers = [1, 2, -1, 3, 0, 4, 5, -20, 6]

print("initial list: ", numbers)
#numbers.sort()
print("sorted list: ", numbers)
numbers.reverse()
print("reversed list: ", numbers)
numbers.append(1000)
print("list with added 1000 on the end: ", numbers)
print("length of the numbers list: ", len(numbers))
print("If 5 si within the numbers list: ", 5 in numbers)
numbers.pop()
print("List after .pop(): ", numbers)
del numbers[0]
print("Deleted [0]: ", numbers)
del numbers[0:2]
print("Deleted [0:2]: ", numbers)
numbers.remove(0)
print("Removed 0: ", numbers)
# numbers.clear()
# print("cleared list: " + str(numbers))

# sets (dont accept dupplicates and are unordered)
numbersSet = {1, 1}
print(numbersSet)

lettersSet = {"A", "A", "B", "B", "B", "C", "C"}
print("First set: ", lettersSet)

lettersSet2 = {"A", "A", "B", "D", "E", "E"}
print("Second set: ", lettersSet2)
print("union: ", lettersSet | lettersSet2)
print("intersection: ", lettersSet & lettersSet2)
print("difference 1 - 2: ", lettersSet - lettersSet2)
print("difference 2 - 1: ", lettersSet2 - lettersSet)

# dictionaries
person = {
    "name": "Jamal",
    "age": 23,
    "address": "Sezamkowa 420"
}

print(person)
print(person["name"])
print(person.get("name"))
print(person.keys())
print(person.values())