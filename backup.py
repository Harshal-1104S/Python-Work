# Import the modules
import time
import random

# Define the questions and answers
questions = [
    {"question": "What is the capital of France?",
        "choices": ["Paris","Berlin", "Rome", "London"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest animal in the world?",
        "choices": ["Elephant", "Whale", "Giraffe", "Dinosaur"],
        "answer": "Whale"
    },
    {
        "question": "What is the name of the largest bone in the human body?",
        "choices": ["Femur", "Humerus", "Tibia", "Fibula"],
        "answer": "Femur"
    },
    {
        "question": "What is the name of the closest star to Earth?",
        "choices": ["Alpha Centauri", "Proxima Centauri", "Sirius", "Sun"],
        "answer": "Sun"
    },
    {
        "question": "What is the name of the largest continent in the world?",
        "choices": ["Africa", "Asia", "Europe", "Australia"],
        "answer": "Asia"
    }
]

# Define a function to start the game
def start_game():
    # Initialize the score and the question index
    score = 0
    question_index = 0
    # Shuffle the questions
    random.shuffle(questions)
    # Loop through the questions
    for question in questions:
        # Print the question and the choices
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")
        # Start the timer
        start_time = time.time()
        # Get the user input
        user_input = input("Enter your answer: ")
        # Stop the timer
        end_time = time.time()
        # Calculate the elapsed time
        elapsed_time = end_time - start_time
        # Check if the user input is valid
        try:
            user_answer = question["choices"][int(user_input) - 1]
        except (ValueError, IndexError):
            user_answer = None
        # Check if the user answer is correct and within the time limit
        if user_answer == question["answer"] and elapsed_time < 10:
            # Increment the score
            score += 1
            # Print a message
            print(f"Correct! You answered in {elapsed_time:.2f} seconds.")
        else:
            # Print a message
            print(f"Wrong! The correct answer is {question['answer']}.")
            print(f"You answered in {elapsed_time:.2f} seconds.")
        # Increment the question index
        question_index += 1
        # Print a blank line
        print()
    # Print the final score
    print(f"Your final score is {score}/{question_index}.")

# Call the start game function
start_game()
