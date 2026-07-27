import requests

def fetch_random_meal():
    url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        meal_data = data["data"]
        meal = meal_data["strMeal"]
        category = meal_data["strCategory"]
        return meal, category
    else:
        raise Exception("Failed to fetch the meal")

def main():
    try:
        meal, category = fetch_random_meal()
        print(f"Meal Type: {meal} \nCategory: {category}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()