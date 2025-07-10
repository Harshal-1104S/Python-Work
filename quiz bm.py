# Importing necessary modules
import pgzrun


# Set the width and height of the game window
WIDTH = 1280
HEIGHT = 720


# Define rectangles for the main box, timer box, and answer boxes
main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)


# Set initial positions for the rectangles
main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)


# Create a list of answer boxes
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]


# Initialize score and time_left variables
score = 0
time_left = 10


# Define quiz questions and their correct answers
q1 = ["What is the capital of France?", "London", "Paris", "Berlin", "Tokyo", 2]
q2 = ["What is 5 + 7?", "12", "10", "14", "8", 1]
q3 = ["What is the 7th month of the year?", "April", "May", "June", "July", 4]
q4 = ["Which planet is the closest to the Sun", "Saturn", "Neptune", "Mercury", "Venus", 3]
q5 = ["Where are the pyramids?", "India", "Egypt", "Morocco", "Canada", 2]


# Create a list of questions
questions = [q1, q2, q3, q4, q5]


# Pop the first question from the list and set it as the current question
question = questions.pop(0)


# Define the draw function to display the game elements
def draw():
    # Fill the screen with a gray background
    screen.fill("dim gray")


    # Draw filled rectangles for the main box and timer box
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")


    # Draw filled rectangles for the answer boxes
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")


    # Display the remaining time in the timer box
    screen.draw.text(str(time_left), (1030, 160), color="black", fontsize=150)


    # Display the current question in the main box
    screen.draw.textbox(question[0], main_box, color="black")


    # Display the answer choices in the answer boxes
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color="black")
        index += 1


# Define the game_over function to display the final score
def game_over():
    global question, time_left, score


    # Create a message with the final score
    message = "Game over. You got %s questions correct" % str(score)


    # Set the message as the current question
    question = [message, "-", "-", "-", "-", 5]


    # Set time_left to 0
    time_left = 0


# Define the correct_answer function to handle correct responses
def correct_answer():
    global question, score, time_left, questions


    # Increment the score
    score += 1


    # If there are more questions, pop the next question and reset the time_left
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        # If no more questions, end the game
        print("End of questions")
        game_over()


# Define the on_mouse_down function to handle mouse clicks on answer boxes
def on_mouse_down(pos):
    index = 1


    # Check if the mouse click is inside any of the answer boxes
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))


            # If the clicked answer is correct, call the correct_answer function
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                # If the clicked answer is incorrect, call the game_over function
                game_over()


        index += 1


# Define the update_time_left function to handle the countdown timer
def update_time_left():
    global time_left


    # If there is time remaining, decrement the time_left
    if time_left:
        time_left -= 1
    else:
        # If time is up, check if there are more questions
        if questions:
            global question
            question = questions.pop(0)
            time_left = 10
        else:
            # If no more questions, end the game
            game_over()


# Schedule the update_time_left function to run every second
clock.schedule_interval(update_time_left, 1.0)


# Run the game
pgzrun.go()
