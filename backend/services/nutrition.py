# class responsbile for finding user's nutrition metrics/goals

class Nutrition():
    def calculate_BMR(self, gender, height, weight, age):
        BMR = 0
        if (gender == "male"):
            BMR = 10*weight + 6.25*height - 5*age + 5
        else:
            BMR = 10*weight + 6.25*height - 5*age - 161

        return BMR

    def calculate_TDEE(self, BMR, activitiy_level):
        if (activitiy_level == 1):
            return BMR * 1.2
        elif (activitiy_level == 2):
            return BMR * 1.375
        elif (activitiy_level == 3):
            return BMR * 1.55
        elif (activitiy_level == 4):
            return BMR * 1.725
        elif (activitiy_level == 5):
            return BMR * 1.9

    def required_calories(self, TDEE, goal):
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

    def calculate_macros(self, TDEE, goal):
        required_calories = self.required_calories(TDEE, goal)
        required_protein = required_calories * 0.30 / 4
        required_carbs = required_calories * 0.40 / 4
        required_fats = required_calories * 0.30 / 9

        return {
            "calories" : required_calories,
            "protein_g" : required_protein,
            "carbs_g" : required_carbs,
            "fats_g" : required_fats
        }




