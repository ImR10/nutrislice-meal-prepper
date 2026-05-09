import requests, json

data = requests.get("https://uga.api.nutrislice.com/menu/api/weeks/school/dining-hall-5/menu-type/breakfast/2026/05/08/?format=json").json()

# returns sections of the JSON response
print(data.keys())
day0 = data['days'][0]
day0_menu = day0['menu_items']

# print(json.dumps(dict(day0_menu[0]), indent=2))

# print each menu item
print(f"\nMenu Items for {day0["date"]}: ")
for item in day0_menu:
    print(item["food"]["name"])

# print menu items less than 300 calories
print("\nFoods <300 Calories: ")
print(f"{'item':<50} {"calories":<20} {"protein"}")
print("*" *80)
for item in day0_menu:
    item_name = item["food"]["name"]
    item_cal = item["food"]["rounded_nutrition_info"].get("calories") or 0
    item_protein = item["food"]["rounded_nutrition_info"].get("protein") or 0
    if (item_cal) <= 300:
        print(f"{item_name:<50} {item_cal:<20} {item_protein}")