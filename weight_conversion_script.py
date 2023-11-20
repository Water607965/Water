weight = input("What's your weight in the unit you currently know? Enter it here: ")

choice = input("What do you want your weight to be measured in? Enter P for pounds and K for kilograms: ")

if choice == "K":
    print(float(weight) * float(0.4535924))

elif choice == "P":
    print(float(weight) * float(2.204623))

print("Verifying your response through your unit...\n")

print("K" or "P" in choice)

print("✅\n")

print("You are successfully verified! We hope that you found this conversion rate successful!\n")

notice = "Note, the program will exit now!\n"

exit()