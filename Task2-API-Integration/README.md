# API Integration Project (Python)
## Overview
This project demonstrates how Python interacts with external APIs and processes JSON data. It includes fetching user data, searching/filtering results, and handling API errors using exception handling.
---
## Objective
To learn how Python communicates with web APIs and how to:

* Send HTTP requests using the `requests` library
* Parse JSON responses
* Apply search/filter logic on data
* Handle API errors using try-except blocks
---
## Features

* Fetch data from a public API
* Parse JSON response into Python objects
* Search user by username
* Display user details (name, email, city)
* Handle invalid API requests and connection errors
---
## Technologies Used

* Python 3
* Requests Library
* JSONPlaceholder API  
  https://jsonplaceholder.typicode.com/users
---
## How to Run the Project
### Step 1: Install Required Library
```bash
pip install requests
```
---
### Step 2: Run the Script
```bash
python api_project.py
```
---
### Step 3: Enter Username When Prompted

### Valid User
```text
Enter username to search: Kamren
User Found
Name: Chelsey Dietrich
Email: Lucio_Hettinger@annie.ca
City: Roscoeview
```

### Invalid User
```text
Enter username to search: abcd
User not found
```
---
### Step 4: Error Handling
If the API URL is incorrect or network fails, the program will not crash. Instead, it shows an error message.

### Example
```text
Error while fetching API data: <connection error message>
```
---
### Project Structure
```text
task2/
│
├── api_project.py
├── README.md
└── screenshots/
    ├── success.png
    ├── not_found.png
    └── error.png
```
---
## Conclusion
This project demonstrates real-world API communication, JSON parsing, filtering, and error handling using Python.
--- 