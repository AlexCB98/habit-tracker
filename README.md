# Pixela Habit Tracker

A simple Python habit tracking project that uses the Pixela API to create and update a visual graph for daily push-up progress.

This project was built using Python, API requests, environment variables, and HTTP methods such as POST, PUT, and DELETE.

---

## Features

- Creates a Pixela user account using an API request
- Creates a Pixela graph for tracking push-ups
- Adds a daily pixel with the number of push-ups completed
- Uses the current date automatically with `datetime`
- Allows user input for daily push-up quantity
- Supports updating an existing pixel
- Supports deleting a pixel from the graph
- Uses environment variables to protect sensitive data
- Sends authenticated requests using custom headers

---

## What I practiced

- Working with external APIs
- Using the `requests` module
- Sending POST, PUT, and DELETE requests
- Using `headers` for API authentication
- Using `.env` files to store private credentials
- Loading environment variables with `python-dotenv`
- Reading secret values with `os.getenv()`
- Formatting dates with `datetime.strftime()`
- Building dynamic API endpoints with f-strings
- Understanding how API endpoints, payloads, and headers work together

---

## Project structure

```
main.py
.env
.gitignore
```

---

## How to run

Before running the project, create a `.env` file and add your Pixela credentials:

```
PIXELA_USERNAME=your_username
PIXELA_TOKEN=your_secret_token
GRAPH_ID=your_graph_id
```

Run the project with:

```bash
python main.py
```

---

## Technologies used

- Python
- Requests
- Pixela API
- python-dotenv
- Environment variables
- datetime
- Git and GitHub

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.