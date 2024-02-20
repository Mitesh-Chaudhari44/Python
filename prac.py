# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 400])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
    pygame.draw.circle(screen, (255, 255, 0), (300,200), 75, draw_top_right=True, draw_bottom_left=True)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()