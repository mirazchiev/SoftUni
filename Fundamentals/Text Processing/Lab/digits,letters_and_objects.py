text = input()

numbers = [number for number in text if number.isdigit()]
chars = [char for char in text if char.isalpha()]
symbols = [symbol for symbol in text if not symbol.isalnum()]

print("".join(numbers))
print("".join(chars))
print("".join(symbols))
