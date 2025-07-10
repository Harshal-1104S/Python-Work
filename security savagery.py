# Import pygame module
import pygame

# Initialize pygame
pygame.init()

# Create a display surface with a size of 300x200 pixels
screen = pygame.display.set_mode((300, 200))

# Load the image file from your directory
background = pygame.image.load("Security Savagery/Backgrounds/loading screen")

# Display the image on the screen
screen.blit(background, (0, 0))

# Update the display
pygame.display.flip()

# Wait for 5 seconds
pygame.time.wait(5000)

# Quit pygame
pygame.quit()
