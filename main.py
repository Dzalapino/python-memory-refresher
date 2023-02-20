from calculator import add

print(add(1, 2))

class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self) -> str:
        return f"Brand: {self.brand}\nprice: {self.price}"

iphone = Phone("Iphone 7+", 300)
motorola = Phone("motorola moto", 210)

print(iphone)
print(motorola)
iphone.call(112)

# working with files
import os.path

filename = "./textFile.txt"
# w - writing, a - appending, r - reading, r+ - reading/writing
if(os.path.isfile(filename)):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")