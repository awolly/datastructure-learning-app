from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Topic, Lesson, QuizQuestion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AnswerSubmission(BaseModel):
    answer: str

@app.get("/")
def home():
    return {"message": "Welcome to the Data Structures Learning App!"}

@app.get("/topics")
def get_topics(db: Session = Depends(get_db)):
    topics = db.query(Topic).all()
    return {"topics": [{"id": t.id, "name": t.name, "description": t.description} for t in topics]}

@app.get("/topics/{topic_id}")
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        return {"error": "Topic not found"}
    lessons = [{"id": l.id, "title": l.title, "content": l.content, "example": l.example} for l in topic.lessons]
    return {"id": topic.id, "name": topic.name, "description": topic.description, "lessons": lessons}

@app.get("/topics/{topic_id}/lessons/{lesson_id}")
def get_lesson(topic_id: int, lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.query(Lesson).filter(Lesson.topic_id == topic_id, Lesson.id == lesson_id).first()
    if not lesson:
        return {"error": "Lesson not found"}
    return {"id": lesson.id, "title": lesson.title, "content": lesson.content, "example": lesson.example}

@app.get("/topics/{topic_id}/quiz")
def get_quiz(topic_id: int, db: Session = Depends(get_db)):
    questions = db.query(QuizQuestion).filter(QuizQuestion.topic_id == topic_id).all()
    if not questions:
        return {"error": "No quiz found for this topic"}
    quiz = [{"id": q.id, "question": q.question, "options": q.options.split(",")} for q in questions]
    return {"quiz": quiz}

@app.post("/topics/{topic_id}/quiz/{question_id}/answer")
def check_answer(topic_id: int, question_id: int, submission: AnswerSubmission, db: Session = Depends(get_db)):
    question = db.query(QuizQuestion).filter(QuizQuestion.id == question_id, QuizQuestion.topic_id == topic_id).first()
    if not question:
        return {"error": "Question not found"}
    correct = submission.answer == question.answer
    return {
        "correct": correct,
        "your_answer": submission.answer,
        "correct_answer": question.answer if not correct else None
    }