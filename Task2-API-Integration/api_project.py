# Import requests library
import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send request to API
    response = requests.get(url, timeout=5)

    # Check for HTTP errors
    response.raise_for_status()

    # Convert JSON response into Python data
    data = response.json()

    # Ask user to enter username
    search_name = input("Enter username to search: ")

    # Variable to check if user exists
    found = False

    # Loop through users
    for user in data:

        # Compare usernames
        if user["username"].lower() == search_name.lower():

            print("\nUser Found")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])

            found = True

    # If user not found
    if not found:
        print("User not found")

# Handle API errors
except requests.exceptions.RequestException as e:
    print("Error while fetching API data:", e)