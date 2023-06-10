number = int(input())
loaded_symbols = int(number / 10)
unloaded_symbols = int(10 - loaded_symbols)
if number == 100:
    print("100% Complete!\n[%%%%%%%%%%]")
else:
    print(f"{number}% [{loaded_symbols * '%'}{unloaded_symbols * '.'}]\nStill loading...")
