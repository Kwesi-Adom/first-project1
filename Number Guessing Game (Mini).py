# Number Guessing Game 

secret_number = 12

guess_number = int(input("Enter the guessing number: "))

if guess_number < secret_number:
  print("Too low")
elif guess_number > secret_number:
  print("Too high")
else:
  print("You got it")