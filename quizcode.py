import pygame, sys
score = 0

class Button():
      def __init__(self, image, pos, text_input, font, base_color, hovering_color):
            self.image = image
            self.x_pos = pos[0]
            self.y_pos = pos[1]
            self.font = font
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                  self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

      def update(self, screen):
            if self.image is not None:
                  screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)

      def checkForInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                  return True
            return False

      def changeColor(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                  self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                  self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load('Background.png')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font('font.ttf', size)

def play():
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        while True:
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

                    # Pop the first question from the list and set it as the current question
                    question = questions.pop(0)

                    draw()

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
                    global time_left, update_time_left

                    update_time_left = 0


                    # If there is time remaining, decrement the time_left
                    if update_time_left:
                        update_time_left -= 1
                    else:
                        # If time is up, check if there are more questions
                        if questions:
                            global question
                            question = questions.pop(0)
                            update_time_left = 10
                        else:
                            # If no more questions, end the game
                            game_over()


                # Schedule the update_time_left function to run every second
                clock.schedule_interval(update_time_left, 1.0)


                # Run the game
                pgzrun.go()






def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(38).render("This is the INSTRUCTIONS screen.", True, "Blue")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)


        INSTRUCTIONS_TEXT = get_font(18).render("Hi gamer! Your objective of this game will be to assess the scenario", True, "Black")
        INSTRUCTIONS_RECT = INSTRUCTIONS_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(INSTRUCTIONS_TEXT, INSTRUCTIONS_RECT)


        INSTRUCTIONS_2_TEXT = get_font(15).render("you are provided with and pick the option you think is best suited with the scenario.", True, "Black")
        INSTRUCTIONS_2_RECT = INSTRUCTIONS_2_TEXT.get_rect(center=(640, 220))
        SCREEN.blit(INSTRUCTIONS_2_TEXT, INSTRUCTIONS_2_RECT)


        INSTRUCTIONS_3_TEXT = get_font(18).render(" You are going to be given 3 scenarios in total. Depending on the", True, "Black")
        INSTRUCTIONS_3_RECT = INSTRUCTIONS_3_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(INSTRUCTIONS_3_TEXT, INSTRUCTIONS_3_RECT)


        INSTRUCTIONS_4_TEXT = get_font(18).render(" options you pick you will be given a different final outcome. Click", True, "Black")
        INSTRUCTIONS_4_RECT = INSTRUCTIONS_4_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(INSTRUCTIONS_4_TEXT, INSTRUCTIONS_4_RECT)


        INSTRUCTIONS_5_TEXT = get_font(18).render("on the back button and then click play to continue!", True, "Black")
        INSTRUCTIONS_5_RECT = INSTRUCTIONS_5_TEXT.get_rect(center=(640, 280))
        SCREEN.blit(INSTRUCTIONS_5_TEXT, INSTRUCTIONS_5_RECT)



        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        PLAY_BUTTON = Button(image=pygame.image.load('Play Rect.png'), pos=(640, 250),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        OPTIONS_BUTTON = Button(image=pygame.image.load('Options Rect.png'), pos=(640, 400),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        QUIT_BUTTON = Button(image=pygame.image.load('Quit Rect.png'), pos=(640, 550),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

pgzrun.go()
