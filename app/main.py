from fastapi import FastAPI, Depends, HTTPException
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from app import models
from app.schemas import WorkoutCreate, WorkoutResponse

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
    db_workout = models.Workout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


@app.get("/workouts")
def get_all_workouts(db: Session = Depends(get_db)):
    return db.query(models.Workout).all()


@app.get("/workouts/{id}")
def get_workout(id: int, db: Session = Depends(get_db)):
    workout = db.query(models.Workout).filter(models.Workout.id == id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@app.delete("/workouts/{id}")
def delete_workout(id: int, db: Session = Depends(get_db)):
    db_workout = db.query(models.Workout).filter(models.Workout.id == id).first()
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    db.delete(db_workout)
    db.commit()
    return {"message": "Workout deleted"}

