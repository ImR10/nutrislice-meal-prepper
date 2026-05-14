import requests, json

data = requests.get("https://uga.api.nutrislice.com/menu/api/weeks/school/dining-hall-5/menu-type/breakfast/2026/05/09/?format=json").json()

# returns sections of the JSON response
print(data.keys())
day0 = data["days"][0]
day0_date = day0["date"]
day0_menu_items = day0["menu_items"]

dates_in_curr_week = []
days = data.get("days")

for date in days:
    dates_in_curr_week.append(date.get("date"))

print(dates_in_curr_week)

num_items = 0
for item in day0_menu_items:
    item_name = item["food"]["name"]
    if item_name.startswith("*"):
        continue
    
    print(f"{item_name}")
    num_items += 1

print(f"\nTotal items: {num_items}\n")

print("menu items with <= 300 calories:")
print(f"{"menu item":<50} {"calories":<20} {"protein":<20} carbs")
print("*" * 100)
for item in day0_menu_items:
    ## use {} to return empty dicts so an empty dict won't crash if .get() is called
    item_food_info = item.get("food", {})
    item_name = item_food_info.get("name") or ""
    item_nutrition = item_food_info.get("rounded_nutrition_info", {})

    item_calories = item_nutrition.get("calories") or 0
    item_protein = item_nutrition.get("g_protein") or 0
    item_carbs = item_nutrition.get("g_carbs") or 0

    if (item_calories) <= 300:
        if (item_calories == "None"):
            item_calories == 0 

        item_protein_str = f"{item_protein}g"
        print(f"{item_name:<50} {item_calories:<20} {item_protein_str:<20} {item_carbs}g ")