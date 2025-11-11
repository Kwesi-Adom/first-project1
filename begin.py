#Question 1 --- checking for an even or odd number

your_number = int(input("enter any number"))

if your_number % 2 == 0:
  print("it is an even number")
  
else:
  print("it is an odd number")

#Question 2 --- checking for positive, zero and negative numbers...

number = float(input("enter a number"))

if number > 0:
  print("it is positive")
elif number == 0:
  print("it is zero")
else:
  print("it is negative")
  
#Question 3 --- checking the largest number taking 3 inputs from a user

number_1 = float(input("enter a number"))
number_2 = float(input("enter a number"))
number_3 = float(input("enter a number"))

if number_1 > number_2 and number_3:
  print(f"{number_1} is the largest in {number_1, number_2, number_3}")
elif number_2 > number_1 and number_3:
  print(f"{number_2} is the largest in {number_1, number_2, number_3}")
elif number_3 > number_1 and number_2:
  print(f"{number_2} is the largest in {number_1, number_2, number_3}")
else:
  print("they are all the same")

#Question 4 --- student grading system

exams_score = int(input("enter your marks..."))

if exams_score >= 80:
  print ("you had an A")
elif exams_score >= 75:
  print ("B+")
elif exams_score >= 70:
  print ("B")
elif exams_score >= 65:
  print ("C+")
elif exams_score >= 60:
  print ("C")
elif exams_score >= 55:
  print ("D+")
elif exams_score >= 50:
  print ("D")
elif exams_score >= 45:
  print ("E")
else:
  print("You have failed")