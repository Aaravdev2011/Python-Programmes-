
name = input("What is your name? ")
mood = input("What's your mood like right now? (happy/sad/tired/stressed/excited): ")
energy = int(input("On a scale of 1 to 10, how is your energy level? "))


if energy < 3:
    print("Notice: It looks like you're running low on fuel. Consider taking a breather.")

if energy >= 5:
    print("You've got plenty of drive to tackle some goals today!")
else:
    print("Keep things gentle today and focus on unwinding.")




if mood == "happy":
    advice = "Ride that wave and share your great vibes with others!"
elif mood == "sad":
    advice = "Reach out to a close friend or lean into a favorite comfort activity."
elif mood == "tired":
    advice = "Hydrate, step away from screens, and give your brain a rest."
elif mood == "stressed":
    advice = "Inhale deeply, pause for a moment, and break your day into tiny steps."
elif mood == "excited":
    advice = "Channel that brilliant momentum into a passion project!"
else:
    advice = "Whatever you're feeling right now is completely valid. Be kind to yourself."



import datetime

today = datetime.datetime.now()


print("\n================================")

print("YOUR PERSONALIZED MOOD ANALYSIS")

print("================================")

print("User:", name)

print("Current Mood:", mood)

print("Energy Score:", energy)
print("Timestamp:", today)

print("Daily Recommendation:", advice)

print("================================")
