

# FastAPI User Authentication API

A FastAPI-based user authentication API with registration, login, and user listing features.

## Features

- User registration: Register a new user with a username, email, and password.
- User login: Authenticate and obtain an access token for accessing protected routes.
- Get users: Retrieve a list of all registered users (protected route).
- JWT Tokens: Secure authentication using JSON Web Tokens (JWT).

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- JWT (PyJWT)
- Passlib
- Uvicorn

## Installation

1. Clone this repository.

```bash
git clone https://github.com/your-username/fastapi-user-authentication.git
```

2. Change the working directory to the project folder.

```bash
cd fastapi-user-authentication
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Run the FastAPI application.

```bash
uvicorn main:app --reload
```

The FastAPI app will run on `http://127.0.0.1:8000`.

## Usage

### Register a New User

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "string",
  "email": "string",
  "password": "string"
}'
```

### Login

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "password": "string"
}'
```

### Get Users (Requires Authorization)

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/getusers' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

Replace `YOUR_ACCESS_TOKEN` with the actual access token obtained during login.

## API Endpoints

### Register a New User

- **URL:** `/register`
- **Method:** POST
- **Request Body:**

```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

- **Response:** User creation confirmation.

### Login

- **URL:** `/login`
- **Method:** POST
- **Request Body:**

```json
{
  "email": "string",
  "password": "string"
}
```

- **Response:** Access and refresh tokens.

### Get Users

- **URL:** `/getusers`
- **Method:** GET
- **Authorization:** Bearer token
- **Response:** List of registered users.

## JWT Tokens

- Access Token: Used for accessing protected routes.
- Refresh Token: Used to obtain a new access token.

## Author

PEAULI

## License

This project is open-source and available under the [MIT License](LICENSE).
```

Please replace `"string"`, `"YOUR_ACCESS_TOKEN"`, and other placeholders with actual values. Also, update the "Author" and "License" sections as needed.
