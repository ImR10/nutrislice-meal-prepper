print("What is your name: ")
name = input()

print("Enter biological gender: ")
gender = input()

print("Enter age: ")
age = float(input())

print("Enter current weight: ")
weight = float(input()) * 0.45359237

print("Enter current height: ")
height = float(input()) * 30.48

print("How active are you? \n1. Sedentary (no exercise)\n2.Lightly Active (1-2x/week)\n3. Moderately Active (3-4x/week)")
print("4. Very active (5-6x/week)\n5. Extremely active (7x/week)")
activity = int(input())

print("What is your goal?")
print("1. Lose Weight (deficit)\n2. Maintain Weight\n3. Gain muscle (surplus)\n4. Agressive Cut\n5. Agressive Bulk")
goal = int(input())

# BMR Calculation (Mifflin-St Jeor Formula)
BMR = 0
if (gender == "male"):
    BMR = 10*weight + 6.25*height - 5*age + 5
else:
    BMR = 10*weight + 6.25*height - 5*age - 161


# TDEE Calculation (Total Daily Energy Expenditure); Maintenence calories
def TDEE_calculation(BMR, activity):
    if (activity == 1):
        return BMR * 1.2
    elif (activity == 2):
        return BMR * 1.375
    elif (activity == 3):
        return BMR * 1.55
    elif (activity == 4):
        return BMR * 1.725
    elif (activity == 5):
        return BMR * 1.9

TDEE = TDEE_calculation(BMR, activity)

def required_calories(TDEE, goal):
    if goal == 1:
        return TDEE-300, TDEE-500
    if goal == 2:
        return TDEE, TDEE
    if goal == 3:
        return TDEE+250, TDEE+500
    if goal == 4:
        return TDEE-500, TDEE-1000
    if goal == 5:
        return TDEE+500, TDEE+1000
    
required_calories1, required_calories2 = required_calories(TDEE, goal)
print(f"Recommended calories/day for {name}: {round(required_calories2)} to {round(required_calories1)} calories /day")