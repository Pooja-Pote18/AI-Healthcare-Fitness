
# Core logic for AI Healthcare & Fitness Project

def calculate_bmi(weight, height_cm):
    """Calculate BMI from weight and height."""
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)


def health_risk(bmi):
    """Return health risk category based on BMI."""
    if bmi < 18.5:
        return "Underweight - Risk of nutritional deficiency."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight - Low health risk."
    elif 25 <= bmi < 29.9:
        return "Overweight - Higher risk of diabetes/heart disease."
    else:
        return "Obese - High risk of chronic diseases."


def workout_plan(goal, activity_level="Medium"):
    """Suggest workout based on goal and activity level."""
    goal = goal.lower()
    if goal == "weight loss":
        return "30 mins brisk walking + 15 mins HIIT daily."
    elif goal == "muscle gain":
        return "45 mins strength training + 20 mins cardio, 5 days a week."
    elif goal == "general fitness":
        return "30 mins moderate exercise (yoga, jogging, cycling) daily."
    else:
        return "Light stretching and daily walks recommended."


def diet_plan(goal):
    """Suggest diet plan based on goal."""
    goal = goal.lower()
    if goal == "weight loss":
        return {
            "Breakfast": "Oats with fruit",
            "Lunch": "Grilled chicken + salad",
            "Dinner": "Veg soup + 2 chapati",
            "Snacks": "Nuts, green tea"
        }
    elif goal == "muscle gain":
        return {
            "Breakfast": "Eggs + whole grain bread",
            "Lunch": "Brown rice + chicken/fish + veggies",
            "Dinner": "Paneer/tofu + salad",
            "Snacks": "Protein shake, nuts"
        }
    else:  # general fitness
        return {
            "Breakfast": "Idli/dosa + chutney",
            "Lunch": "Rice + dal + veggies",
            "Dinner": "Soup + chapati",
            "Snacks": "Fruit, sprouts"
        }


def timeframe_suggestion(goal):
    """Suggest timeframe to achieve the goal."""
    goal = goal.lower()
    if goal == "weight loss":
        return "Follow strict routine for 3 months to reduce 5-8 kg."
    elif goal == "muscle gain":
        return "Follow routine for 6 months to see visible muscle growth."
    else:
        return "Maintain consistency for lifelong fitness."


def generate_4_week_daily_plan(goal):
    """
    Generate a simple 4-week daily plan for workout and diet.
    Returns a list of dictionaries with week, day, workout, and diet.
    """
    goal = goal.lower()
    if goal == "weight loss":
        workout = "30 mins brisk walking + 15 mins HIIT"
        diet = "Oats (breakfast), Salad (lunch), Veg soup (dinner)"
    elif goal == "muscle gain":
        workout = "45 mins strength training + 20 mins cardio"
        diet = "Eggs (breakfast), Chicken/fish + rice (lunch), Paneer + salad (dinner)"
    else:  # general fitness
        workout = "30 mins yoga or cycling"
        diet = "Idli/dosa (breakfast), Dal + rice (lunch), Soup + chapati (dinner)"

    plan = []
    for week in range(1, 5):
        for day in range(1, 7 + 1):  # 7 days
            plan.append({
                "week": week,
                "day": day,
                "workout": workout,
                "diet": diet
            })
    return plan
