# Reservation Service

The Reservation Service manages reservation-related operations. It is a microservice designed to work independently or as part of a larger application. This service is built using Flask and Docker, with data stored in a SQLite database.


## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Initialization](#database-initialization)
- [Running the Service](#running-the-service)


## Installation

1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/Natazja/reservations_service.git>
   cd reservation-service

2. **Install Dependencies: Install the required Python packages by running**:
   ```bash
   pip install -r requirements.txt


## Setup
The project uses Docker for containerization and SQLite for data storage.

1. **Database Setup**: Ensure you have the database.db file or run the provided import_json.py script to create and populate it.

2. **Docker Setup**: Build the Docker image for the reservation service.
   ```bash
   docker build -t reservation-microservice .

3. **Environment Variables**:

FLASK_ENV: Set to production to run the app in production mode.
FLASK_APP: Set to app.py to specify the entry point of the Flask application.


## Usage
1. **Starting the Service**: Run the following command to start the Docker container:
   ```bash
   docker run -p 5000:5000 reservation-microservice

2. **Testing the Service**: Access the API at http://localhost:5000 to test various endpoints.


## API Endpoints
The following endpoints are available in the Reservation Service:

### CRUD Operations for Reservations
**GET /reservations**
Retrieve all reservations.

**Response**: JSON array of all reservations.

**GET /reservations/<id>**
Retrieve a specific reservation by ID.

**Parameters**: id (integer) - the ID of the reservation.
**Response**: JSON object of the reservation.

**POST /reservations**
Create a new reservation.

**Request Body**: JSON object with reservation details.
**Response**: JSON object of the newly created reservation.

**PUT /reservations/<id>**
Update a reservation by ID.

**Parameters**: id (integer) - the ID of the reservation.
**Request Body**: JSON object with updated reservation details.
**Response**: JSON object of the updated reservation.

**DELETE /reservations/<id>**
Delete a reservation by ID.

**Parameters**: id (integer) - the ID of the reservation.
**Response**: Success message.


## Database Initialization
To initialize the database with sample data:

1. **Run the Database Initialization Script**: If your database is empty or needs to be initialized, run the import_json.py script to populate it with sample data from reservation_data.json.
   ```bash
   python import_json.py

2. **Using Docker for Database Initialization**: If running in Docker, you can initialize the database by mounting it into the container and running the script:
   ```bash
   docker run -it --rm -v $(pwd)/database.db:/app/database.db reservation-microservice python import_json.py


## Running the Service
1. **Start the Application**: Once the database is initialized, start the application using Docker:
   docker run -p 5000:5000 reservation-microservice

2. **Access the API**: Open http://localhost:5000 in your browser or use a tool like Postman to interact with the API.

   



   
