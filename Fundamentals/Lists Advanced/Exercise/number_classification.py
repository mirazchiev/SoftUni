numbers = list(map(int, input().split(", ")))
positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(f"Positive: {', '.join(map(str, positive_numbers))}\nNegative: {', '.join(map(str, negative_numbers))}"
      f"\nEven: {', '.join(map(str, even_numbers))}\nOdd: {', '.join(map(str, odd_numbers))}")
