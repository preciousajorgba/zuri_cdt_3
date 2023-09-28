

# FastAPI User Signup and Information API

The **FastAPI User Signup and Information API** is a simple web service built using the FastAPI framework that allows users to sign up, obtain authentication tokens, and retrieve user information. This documentation provides detailed information on how to interact with the API, including endpoints, data models, and example requests.

**Live API URL:** [https://task3-j2mm.onrender.com]

## Overview

The FastAPI User Signup and Information API serves as a demonstration of how to create a user authentication system with FastAPI and SQLAlchemy. It includes two primary endpoints:

1. **Signup**: Allows users to create a new account. Upon successful registration, the user receives an authentication token.

2. **User Information**: Enables users to retrieve their own information using their authentication token.

## Endpoints

The API has the following endpoints:

- **POST /signup** - User registration endpoint
- **GET /user** - Retrieve user information

## Data Models

### UserCreate

- **username (str)**: The desired username for registration.
- **password (str)**: The user's chosen password.

### Token

- **access_token (str)**: The authentication token issued upon successful registration.
- **token_type (str)**: The type of token (usually "bearer").
- **username (str)**: The username of the user.
- **id (int)**: The user's ID.
- **status_code (int)**: The HTTP status code of the response.

### UserInDB

- **id (int)**: The user's unique identifier.
- **username (str)**: The user's username.
- **password (str)**: The hashed password (not returned by default).

## Authentication and Security

- Authentication tokens are issued using the **HS256** algorithm and a secret key.
- Passwords are hashed using the **bcrypt** algorithm for security.

## How to Test the API Locally

To test the API locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-user-signup.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-user-signup
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI application locally:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

## Example API Requests

### Signup

To sign up a new user, make a POST request to the `/signup` endpoint. Replace `"your-username"` and `"your-password"` with your desired username and password:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "your-username",
    "password": "your-password"
  }'
```

The server will respond with a token if the signup is successful.

### Retrieve User Information

To retrieve user information, make a GET request to the `/user` endpoint. Replace `4` with the user's `id` and `"TOKEN"` with a valid user token:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/user?id=4&token=TOKEN' \
  -H 'accept: application/json'
```

The server will respond with the user's information if the token is valid.

## Testing the Live API

You can also test the live API using the provided URL:

**Live API URL:** [https://task3-j2mm.onrender.com](https://task3-j2mm.onrender.com)

Follow the same example API requests as outlined above, but replace the base URL with the live URL.

## Important Notes

- This project is intended for learning and testing purposes. It uses SQLite as the database backend and should not be used in production without further security considerations and configuration.

- Detailed documentation for the endpoints, request/response data, and database structure can be found within the respective files in this repository.

For more details about FastAPI and SQLAlchemy, refer to the official documentation:

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)


