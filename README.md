# workout-tracker
Workout Tracker REST API using FastAPI + SQLite

## Tech Stack
Language: Python
Tools/Frameworks: FastAPI, SQLAlchemy, SQLite, Pydantic, Uvicorn

## Overview 
The program allows you to record workouts via an SQL database. The FastAPI allows you to add your workouts, get workouts and delete workouts.

## Features
- `POST /workouts` — log a new workout
- `GET /workouts` — retrieve all workouts
- `GET /workouts/{id}` — retrieve a specific workout by ID
- `DELETE /workouts/{id}` — delete a workout by ID

## How to run
1. Clone the github repository. 
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn app.main:app --reload`
5. Visit `http://127.0.0.1:8000/docs` to interact with the API

## What I Learned
Building this project gave me a practical understanding of how REST APIs work. I also learned how to structure a FastAPI application across multiple 
files, connect it to a database using SQLAlchemy and use Pydantic 
schemas to validate data input and output. I also gained an understanding 
of how HTTP methods map to CRUD operations, and how dependency injection works 
in FastAPI to manage database sessions cleanly.

