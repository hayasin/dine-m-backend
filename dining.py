import requests

def make_api_request(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return None

# Function to get menu for a specific day, meal, and dining hall
def get_menu(entries, date, meal, dining_hall):
    menu = []
    for entry in entries:
        if entry['date'] == date and meal in entry['mealNames'] and entry['diningHallName'] == dining_hall:
            menu.append(entry['itemName'])
    return menu


def api_call():
    api_url = "https://michigan-dining-api.tendiesti.me/v1/all"
    response_data = make_api_request(api_url)
    return response_data

# # Example API call
# api_url = "https://michigan-dining-api.tendiesti.me/v1/all"
# response_data = make_api_request(api_url)

# if response_data and 'filterableEntries' in response_data:
#     filterableEntries = response_data['filterableEntries']

#     # Define the date, meal, and dining hall you are interested in
#     date = "2024-05-01"
#     meal = "BREAKFAST"
#     dining_hall = "South Quad Dining Hall"

#     # Fetch the menu
#     menu = get_menu(filterableEntries, date, meal, dining_hall)
#     print("Menu for", meal, "at", dining_hall, "on", date, ":", menu)
# else:
#     print("Failed to retrieve or parse dining hall data.")
