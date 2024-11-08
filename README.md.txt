# Django API for Transactions

This project provides a REST API for managing and retrieving transactions for clients. It supports filtering by `client_id` and optional date range (`start_date` and `end_date`). The API is built using Django and Django REST Framework (DRF), with token-based authentication (JWT).

## Features
- Retrieve transactions by `client_id` and date range.
- JWT-based authentication for secure access.
- Custom error handling for validation errors.
- Optional date range filtering for transactions.

## Setup Instructions

### Step 1: Create a Virtual Environment
1. In your project directory, create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    - **On macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```
    - **On Windows**:
      ```bash
      venv\Scripts\activate
      ```

### Step 2: Install Required Dependencies
Install the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### Step 3: Configure the Database
Update the database settings in `data_engineering_project/settings.py` to connect to your PostgreSQL database. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory to store environment-specific settings, like the secret key and database configurations. Example:
    ```plaintext
    SECRET_KEY=your-secret-key
    DATABASE_URL=your-database-url
    ```

## Running the Application
Start the Django development server:
    ```bash
    python manage.py runserver
    ```
The application will run on `http://127.0.0.1:8000` by default.

## Running the API
- **Endpoint**: `http://127.0.0.1:8000/api/transactions/<client_id>/`
- **HTTP Method**: `GET`
- **Query Parameters**:
  - `start_date` (optional, format: `YYYY-MM-DD`)
  - `end_date` (optional, format: `YYYY-MM-DD`)

**Example Request**:
GET /api/transactions/12345/?start_date=2023-01-01&end_date=2023-12-31

JWT authentication is required. Pass the token in the `Authorization` header like this:
Authorization: Bearer <your-jwt-token>


## ETL Process
(If applicable, describe your ETL steps here, or remove this section if there is no ETL process.)

1. Ensure the CSV files are in the root directory.
2. Run the ETL script with:
    ```bash
    python manage.py run_etl
    ```

## Optional: Dockerization Instructions
To run the application with Docker:

### Step 1: Build the Docker Image
Ensure you have a `Dockerfile` in the project root directory, then run:
    ```bash
    docker build -t django-api .
    ```

### Step 2: Docker Compose
If you have a `docker-compose.yml` file, you can run both Django and PostgreSQL with one command:
    ```bash
    docker-compose up --build
    ```
This will start all services in the `docker-compose.yml` file, including the Django app and PostgreSQL database.

## Required Dependencies
These dependencies are required to run the project. They are listed in `requirements.txt`.

- Django
- Django REST Framework (DRF)
- djangorestframework-simplejwt (for JWT-based authentication)
- psycopg2 (PostgreSQL database adapter for Django)
- python-dotenv (for loading environment variables)

Install them all by running:
    ```bash
    pip install -r requirements.txt
    ```

## Additional Notes

### Authentication
JWT authentication is used for secure API access. Make sure to generate a JWT token after user authentication to interact with the API.

### Error Handling
Custom error responses are implemented for missing parameters, incorrect data formats, and unauthorized access.

### Troubleshooting
- **Database Connection Issues**: Ensure the PostgreSQL server is running and the database credentials are correct in the settings.
- **Token Errors**: Verify the token is valid and not expired; regenerate if necessary.

### Testing
To run tests:
    ```bash
    python manage.py test
    ```


