# quiz_game.py

def display_question(question, options, correct_answer):
    print(f"\n{question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Enter the number of your answer: ")
    return user_answer == correct_answer

def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "3"  # Intentional logic error: correct answer should be 2
        },
        {
            "question": "What is 5 + 7?",
            "options": ["10", "11", "12", "13"],
            "answer": "3"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
            "answer": "1"
        }
    ]
    
    score = 0  # Intentional run-time error: initialize as "None" to cause a crash
    print("Welcome to the Quiz Game!")

    for q in questions:
        if display_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1  # Logic error: incorrect scoring
        else:
            print("Wrong answer.")

    print(f"\nYour final score is {score}/{len(questions)}.")  # Intentional syntax error: missing closing quote

if __name__ == "__main__":
    quiz_game()
