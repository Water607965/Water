#an example of functions. Although it's not perfect, please inference from it.



print("Hello, welcome!")

name = input("What's your name?\n")

if name == "Ankur Jain":
    test = input("Are you evil or no?\n")
    if test == "yes":
        print("You are a banned user from our area. Please proceed to the exit!")
        exit()
    else:
        print("We've underestimated you. You may enter.")

print("Before you enter our establishment, we need your real age to confirm that you are not a minor.\n")

age = input("What's your birth year?\n")

real_age = 2023-float(age)

if real_age > 13:
    check = "You are suitable to enter our establishment, since you are not a minor.\n"
    print(check)
    print("Verifying your response...\n")
    print("suitable" in check)
    print("You are successfully verified! You may now enter our establishment.\n")
elif real_age <= 13:
    kick = "You are not suitable to enter our establishment based off of your age.\n"
    print("Verifying your inputted response...\n")
    print("Fit to enter establishment" in kick)
    print(kick)
    rule = "minors under the age of 13 cannot enter our establishment"
    print("As a result of our rule that states that " + rule + ", you are not suitable to enter this establishment.\n")
    exit()
menu = "food\nwater\nbread\n"
print(f"{name}, here we have some options for you. We have:\n{menu}")

price = 100

f = input("What do you desire out of our menu?\n")

quantity = input("How much of your specified order do you want?\n")

total = price * int(quantity)

print(f"Thank you! Your total is: ${str(total)}")

print(f"Alright {name}, we have your order for {quantity}  {f}'s + submitted. Its going to be ready soon for you!\n")

print(f"Hello, {name}, here is your {f}. We hope that you had a great time at our establishment.\n")

print(f"However, {name}, do you want to know how much letters your name possesses, as a funny reminder?\n")

maybe = input("Type and enter yes or no here: \n")

t = "Totally not an establishment.\n"

if maybe == "no":
    print(f"Alright, + {name}, you can leave our establishment now. Have a great rest of your day.\n")
    exit()
if maybe == "yes":
    print(len(name))
    exit()