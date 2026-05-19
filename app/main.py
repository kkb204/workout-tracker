from fastapi import FastAPI, Depends
from app.database import engine, SessionLocal
from app import models
from app import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message" : "Workout Tracker API"}

@app.post("/workouts")
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    # logic here


@app.get("/workouts")
def get_workout(workout: WorkoutResponse, db: Session = Depends(get_db)):
    # logic here