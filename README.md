# Library_Management_System_API
 
This project implements a Library Management System API using FastAPI and MongoDB as the database. It provides endpoints to perform CRUD operations on users.

## Tech Stack
* Language: Python
* Framework: FastAPI
* Database: MongoDB (MongoDB Atlas M0 Free Cluster)

## Setup
1. Clone the repository:

  ```bash
  git clone https://github.com/Maanas74/library-management-system.git)
```

2. Install dependencies:

```bash
cd library-management-system
pip install -r requirements.txt)
```

3. Configuration:

* Rename .env.example to .env and provide your MongoDB Atlas connection string.
* Ensure you have a MongoDB Atlas M0 Free Cluster set up.

4. Run the application:

```bash
uvicorn main:app --reload
```

This command will start the FastAPI application locally.

## API Endpoints
The API provides the following endpoints:

* GET /students : Get all students, or on the basis of country or age filter.
* GET /students/{id} : Get details of a specific student.
* POST /students : Add a new student.
* PATCH /students/{id} : Update details of a specific student.
* DELETE /students/{id} : Delete a specific student.
