# main.py

from flask import Flask
from models import Base
from database import engine
from backend.question_service import router as question_router

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

app.register_blueprint(question_router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
