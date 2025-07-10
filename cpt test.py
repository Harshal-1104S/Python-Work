# Import pygame module for graphics and sound
import pygame

# Initialize pygame
pygame.init()

# Create a screen with width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# Set the title and icon of the window
pygame.display.set_caption("Safe N Secure")
icon = pygame.image.load("lock.png") # Load an image file for the icon
pygame.display.set_icon(icon)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define some fonts
title_font = pygame.font.SysFont("arial", 64)
text_font = pygame.font.SysFont("arial", 32)

# Define some sounds
win_sound = pygame.mixer.Sound("win.wav") # Load a sound file for winning
lose_sound = pygame.mixer.Sound("lose.wav") # Load a sound file for losing
click_sound = pygame.mixer.Sound("click.wav") # Load a sound file for clicking

# Define some variables
score = 50 # The user's score
question = 0 # The current question number
running = True # The game loop flag
game_over = False # The game over flag

# Define a list of questions and answers
# Each question is a tuple of (question text, correct answer, wrong answer, correct feedback, wrong feedback)
questions = [
    ("You receive an email from your bank asking you to verify your account details. What do you do?",
     "Ignore the email and report it as spam.",
     "Click on the link and enter your information.",
     "That's right! This is a phishing attempt to steal your personal information. Never click on suspicious links or attachments in emails.",
     "Oops! This is a phishing attempt to steal your personal information. Never click on suspicious links or attachments in emails."),
    ("You want to download a new game from the internet. What do you do?",
     "Check the source of the download and scan the file for viruses before opening it.",
     "Download the file from any website and open it without scanning it.",
     "That's right! You should always be careful about what you download from the internet and scan the files for viruses before opening them.",
     "Oops! You should always be careful about what you download from the internet and scan the files for viruses before opening them."),
    ("You are browsing the web and see an ad that says you have won a free iPhone. What do you do?",
     "Close the ad and ignore it.",
     "Click on the ad and enter your personal details to claim the prize.",
     "That's right! This is a scam to trick you into giving away your personal details or paying for something you will never receive. Never trust ads that offer something too good to be true.",
     "Oops! This is a scam to trick you into giving away your personal details or paying for something you will never receive. Never trust ads that offer something too good to be true."),
    ("You are using a public Wi-Fi network at a coffee shop. What do you do?",
     "Use a VPN to encrypt your data and avoid accessing sensitive websites or apps.",
     "Use the network without a VPN and access your online banking or shopping accounts.",
     "That's right! You should always use a VPN to protect your data when using a public Wi-Fi network. You should also avoid accessing sensitive websites or apps that require your personal information.",
     "Oops! You should always use a VPN to protect your data when using a public Wi-Fi network. You should also avoid accessing sensitive websites or apps that require your personal information."),
    ("You are creating a new account on a website. What do you do?",
     "Use a strong and unique password that contains letters, numbers and symbols.",
     "Use a weak and common password that is easy to remember or reuse an old password.",
     "That's right! You should always use a strong and unique password for each of your online accounts. This will make it harder for hackers to crack your password and access your information.",
     "Oops! You should always use a strong and unique password for each of your online accounts. This will make it harder for hackers to crack your password and access your information.")
]

# Define a function to draw the screen
def draw_screen():
    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the title text
    title_text = title_font.render("Safe N Secure", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (400, 100)
    screen.blit(title_text, title_rect)

    # Draw the score text
    score_text = text_font.render(f"Score: {score}", True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.center = (400, 200)
    screen.blit(score_text, score_rect)

    # Draw the question text
    question_text = text_font.render(questions[question][0], True, WHITE)
    question_rect = question_text.get_rect()
    question_rect.center = (400, 300)
    screen.blit(question_text, question_rect)

    # Draw the answer buttons
    pygame.draw.rect(screen, GREEN, (100, 400, 300, 100)) # Draw a green rectangle for the correct answer
    pygame.draw.rect(screen, RED, (400, 400, 300, 100)) # Draw a red rectangle for the wrong answer
    correct_text = text_font.render(questions[question][1], True, BLACK) # Render the correct answer text
    correct_rect = correct_text.get_rect()
    correct_rect.center = (250, 450)
    screen.blit(correct_text, correct_rect) # Blit the correct answer text
    wrong_text = text_font.render(questions[question][2], True, BLACK) # Render the wrong answer text
    wrong_rect = wrong_text.get_rect()
    wrong_rect.center = (550, 450)
    screen.blit(wrong_text, wrong_rect) # Blit the wrong answer text

    # Update the display
    pygame.display.update()

# Define a function to check the user's input
def check_input():
    global score # Use the global score variable
    global question # Use the global question variable
    global game_over # Use the global game_over variable
    # Loop through the events
    for event in pygame.event.get():
        # If the user clicks the close button, quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # If the user clicks the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # If the mouse is over the correct answer button
            if 100 <= mouse_x <= 400 and 400 <= mouse_y <= 500:
                # Play the click sound
                click_sound.play()
                # Increase the score by 10
                score += 10
                # Show the correct feedback
                show_feedback(questions[question][3])
            # If the mouse is over the wrong answer button
            if 400 <= mouse_x <= 700 and 400 <= mouse_y <= 500:
                # Play the click sound
                click_sound.play()
                # Decrease the score by 10
                score -= 10
                # Show the wrong feedback
                show_feedback(questions[question][4])
            # Check if the game is over
            check_game_over()

# Define a function to show the feedback
def show_feedback(feedback):
    # Draw the feedback text
    feedback_text = text_font.render(feedback, True, WHITE)
    feedback_rect = feedback_text.get_rect()
    feedback_rect.center = (400, 550)
    screen.blit(feedback_text, feedback_rect)
    # Update the display
    pygame.display.update()
    # Wait for 2 seconds
    pygame.time.wait(2000)

# Define a function to check if the game is over
def check_game_over():
    global score # Use the global score variable
    global question # Use the global question variable
    global game_over # Use the global game_over variable
    # If the score is 100 or more, the user wins
    if score >= 100:
        # Play the win sound
        win_sound.play()
        # Show the win message
        show_message("You win! You are safe and secure online.")
        # Set the game over flag to True
        game_over = True
    # If the score is 0 or less, the user loses
    elif score <= 0:
        # Play the lose sound
        lose_sound.play()
        # Show the lose message
        show_message("You lose! You got hacked.")
        # Set the game over flag to True
        game_over = True
    # If the score is between 0 and 100, the game continues
    else:
        # Increase the question number by 1
        question += 1
        # If there are no more questions, the game ends
        if question >= len(questions):
            # Show the end message
            show_message("The game is over. Your final score is " + str(score) + ".")
            # Set the game over flag to True
            game_over = True

# Define a function to show a message
def show_message(message):
    # Fill the screen with black
