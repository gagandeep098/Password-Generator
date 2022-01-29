import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "#*@$"
all = letters + letters.lower() + numbers + symbols
length = int (input("enter password length: "))
print("your password")
password = "".join(random.sample(all, length))
print(password)