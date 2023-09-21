import pygame
import random
from Speech import get_speech

# Match cases for speech
match_row = ['1', '2', '3', '4', '5', 'exit']
match_col = ['1', '2', '3', '4', '5', 'exit']
match_color = ['yes', 'no']
match_mode = ['speech', 'mouse']

print("Welcome to speech driven wackamole! When promted for information, speak your answer one time clearly, and wait for it to be processed. Thank you, and enjoy! \n")
while True:
    print("This game requires identifying red and green. Would you like to turn on color contrast mode? (For deuteranomaly, protanomaly, protanopia and deuteranopia) Say 'yes' or 'no'")
    color_access = get_speech(match_color)
    if color_access != 'Error':
        break

if color_access == 'yes':
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (255, 165, 0)
    RED = (0, 0, 255)  
else:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

while True:
    print("\nWould you like to proceed with speech input, or switch to mouse driven commands? (Say Speech or Mouse)")
    mode = get_speech(match_mode)
    if mode != 'Error':
        break

# Instructions
if mode == 'mouse':
    print("\nHow to play: whack the mole by clicking on the colored square!")
else:
    print("\nHow to play: whack the mole by telling the computer what square he is on! Press any key to begin, and any key to make your next square choice. If your speech is not decipered properly, you will be reprompted.")

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(5):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#0 is white, 1 green, 2 red
genRow = random.randint(0,4)
genCol = random.randint(0,4)
grid[genRow][genCol] = 2
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [130, 130]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Whackamole")
 
# Loop until the user clicks the close button.
done = False
white = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done and white:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if mode == 'mouse':
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
            elif mode == 'speech':
                print("\n")
                while True:
                    print("Speak Row (Say exit to quit)")
                    row = get_speech(match_row)
                    if row == 'exit':
                        done = True
                        break
                    elif row != "Error":
                        row = int(row) - 1
                        break
                if done:
                    break
                while True:
                    print("Speak Column (Say exit to quit)")
                    column = get_speech(match_col)
                    if column == 'exit':
                        done = True
                        break
                    elif column != "Error":
                        column = int(column) - 1
                        break
                if done:
                    break

            # Set the locations
            if grid[row][column] == 2:
                grid[row][column] = 1
                generate = True
                while generate:
                    genRow = random.randint(0,4)
                    genCol = random.randint(0,4)
                    if grid[genRow][genCol] == 0:
                        grid[genRow][genCol] = 2
                        generate = False
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    white = False
    for row in range(5):
        for column in range(5):
            if grid[row][column] == 0:
                color = WHITE
                white = True
            elif grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()