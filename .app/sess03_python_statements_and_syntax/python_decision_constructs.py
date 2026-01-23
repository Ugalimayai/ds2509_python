# this script/file demonstrates Python's selection/decision/conditional constructs

#import the sys module
import sys

# 1. if
temperature = float(input("Please enter today's temperature in degrees Celsius: \n"))
if temperature > 25:
    print(f"Hooray 🎉🎉, it's a warm day, let's head to the beach🍹🍹!")

password = ""
if password == "":
    print(f"Please enter your password.")

#2. if..else
user_num = int(input("Please enter your number and I'll tell you if it's odd or even:\n"))
if user_num % 2 == 0:
    print(f"{user_num} is an even number.")
else:
    print(f"{user_num} is an odd number.")

score = int(input("Please enter your score in the exam:\n"))
if score >= 50:
    print(f"Congratulations! With a score of {score}, You passed the exam!")
else:
    print(f"Unfortunately, with a score of {score}, you've failed the exam!")

# 3. if...elif (else if)...else
#Grade the student based on their score
if score >= 70 and score <= 100:
    print(f"With a score of {score}, you got grade A.")
elif score >= 60 and score <= 69:
    print(f"With a score of {score}, you got grade B.")
elif score >= 50 and score <= 59:
    print(f"With a score of {score}, you got grade C.")
elif score >=40 and score <=49:
    print(f"With a score of {score}, you got grade D.")
elif score >=0 and score <=39:
    print(f"With a score of {score}, you got grade E.")
else:
    print(f"Sorry, {score} is not a valid score."
          f"\nPlease enter a score between 0 and 100.")
    sys.exit() #terminate the script as user provided invalid input

# 4. match
# NB: match works in python 3.10 and above. Match is similar to 'switch' in C and its derived languages
# Give the student a comment based on their score using 'match'
match score:
   case score if score >= 70:
      print("Excellent Job!")
   case score if score >= 60:
      print(f"Very Good!")
   case score if score >= 50:
      print(f"Good!")
   case score if score >= 40:
      print(f"Fair!")
   case score if score >= 0:
      print(f"Try harder next time!")

day = input("Please enter a day of the week:\n")
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")
    case _:
        print(f"Sorry, {day} is not a valid day of the week.")
        sys.exit() # Terminate the script as the user gave invalid output

