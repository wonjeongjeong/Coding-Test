# 28702번 FizzBuzz
game = []
for i in range(3):
    string = input()
    game.append(string)

for word in game:
    if word == "FizzBuzz":
        continue
    elif word == "Fizz":
        continue
    elif word == "Buzz":
        continue
    else:
        i = int(word)
        index = game.index(word)
        number = i + 3 - index
        break

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0 and number % 5 != 0:
    print("Fizz")
elif number % 3 != 0 and number % 5 == 0:
    print("Buzz")
else:
    print(number)