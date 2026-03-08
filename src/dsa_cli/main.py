from pathlib import Path
from loader import load_question, Question
from display import show_question
import json

BASE_DIR = Path(__file__).parent    
QUESTION_PATH = BASE_DIR / '../../questions/questions.json'

def main():
    print("Hello from personal-project!")


if __name__ == "__main__":
    main()
