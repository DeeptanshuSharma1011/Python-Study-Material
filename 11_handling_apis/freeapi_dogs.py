import requests

def fetch_random_dog():
    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        dog_data = data["data"]
        name = dog_data["name"]
        life = dog_data["life_span"]
        return name, life
    else:
        raise Exception("Failed to fetch the dog")

def main():
    try:
        name, life = fetch_random_dog()
        print(f"Name of the dog: {name} \nLife span of the dog: {life}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()