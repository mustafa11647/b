
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60
SPEED = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce")

# Ball properties
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [SPEED, SPEED]

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Bounce off the walls
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
        BALL_COLOR = random_color()
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        BALL_COLOR = random_color()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
