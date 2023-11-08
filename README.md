# my-movie-api

## Description

This project is a Python-based movie API, powered by FastAPI, designed to perform essential CRUD operations: Create, Read, Update, and Delete for movie data, along with user authentication through JWT. The API enables users to interact with movie records, including creating, retrieving, updating, and deleting movie data, and authenticated users can access a comprehensive list of registered movies.

## Technologies Used

Python: The core language used for building the application.
FastAPI: A modern and efficient web framework for creating APIs.
SQLAlchemy: A powerful SQL toolkit for interacting with databases.
JWT Authentication: JSON Web Tokens (JWT) for secure user authentication.

## Installation
1. Ensure you have Python 3.10 or a higher version installed.
2. Begin by cloning the project repository.
3. Create a dedicated virtual environment for this project to manage dependencies cleanly.
4. Install the required packages listed in the requirements.txt file using the following command:
`pip install -r requirements.txt`.

## Usage
1. Launch the server by executing the command `uvicorn main:app --reload`.
2. To access the interactive documentation, navigate to `http://localhost/docs`.
3. For login purposes, the default user credentials are as follows:
Email: 'admin@gmail.com'
Password: 'admin'
4. You can use the token generated from the login to access the movie data, add new movies, update existing movies, and delete movies.