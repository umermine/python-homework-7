#Adding variables
age = int(input("Enter your age "))
#Writing code
if age > 10:
    if age < 20:
        print("You are allowed and your age is between 10 and 20.")
    else:
        print("You are not allowed because your age is 20 or older.")
else:
    print("You are not allowed because your age is 10 or younger.")
