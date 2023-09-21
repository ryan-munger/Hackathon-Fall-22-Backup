from tkinter import HORIZONTAL
import pygame
from Grid import Grid
from Toggle import Toggle
from Ship import Ship
from random import randint
from Speech import get_speech


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (155, 155, 155)
BLUE = (0,0,255)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
# This sets the margin between each cell
MARGIN = 5
grid = Grid(size=10, GREEN=GREEN, MARGIN=MARGIN, HEIGHT=HEIGHT, WIDTH=WIDTH, WHITE=WHITE, GREY=GREY, RED=RED, BLUE=BLUE)

voice_toggle = Toggle('voice', x_start=300, y_start=75, width=50, height=50, activated=False)

vertical_toggle = Toggle('vertical', x_start=300, y_start=10, width=50, height=50)
ships = [Ship(5), Ship(4), Ship(3), Ship(3), Ship(2)]

ships_enemy = [Ship(5), Ship(4), Ship(3), Ship(3), Ship(2)]
enemy_grid = Grid(size=10, GREEN=GREEN, MARGIN=MARGIN, HEIGHT=HEIGHT, WIDTH=WIDTH, WHITE=WHITE, GREY=GREY, RED=RED, BLUE=BLUE)

for i in range(len(ships_enemy)):
    orientations = [['vertical', [0,1]], ['horizontal', [1,0]]]
    orientation, iteration = orientations[randint(0,1)]
    while True:
        x = randint(0,9)
        y = randint(0,9)
        if ships_enemy[0].ship_to_grid(head=(x,y), orientation=orientation, grid=enemy_grid.grid):
            for i in range(ships_enemy[0].size):
                enemy_grid.grid[x][y] = 4
                x += iteration[0]
                y += iteration[1]
            ships_enemy.pop(0)
            break


# Initialize pygame
pygame.init()


# font style
font = pygame.font.Font('freesansbold.ttf', 25)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    toggles = Toggle.toggles

    for event in pygame.event.get():  # User did something
        
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if grid.is_clicked(pos) and not toggles['voice'].activated:
                # Change the x/y screen coordinates to grid coordinates
                x = pos[0] // (WIDTH + MARGIN)
                y = pos[1] // (HEIGHT + MARGIN)
                # for when doing the ship selection
                if ships:
                    if toggles['vertical'].activated:
                        iteration = [0, 1]
                        orientation = 'vertical'
                    else:
                        iteration = [1, 0]
                        orientation = 'horizontal'
                    if ships[0].ship_to_grid((x, y), orientation, grid.grid):
                        for i in range(ships[0].size):
                            grid.grid[x][y] = 3
                            x += iteration[0]
                            y += iteration[1]
                            
                        ships.pop(0)
                # for when doing enemy ship guesses
                else:
                    if enemy_grid.grid[x][y] == 6 or enemy_grid.grid[x][y] == 5:
                        pass
                    elif enemy_grid.grid[x][y] == 4:
                        enemy_grid.grid[x][y] = 5
                    else:
                        enemy_grid.grid[x][y] = 6
                        if enemy_grid.check_over():
                            print("You Won!!!!!")
                            pygame.quit()
                        while True:
                            x = randint(0,9)
                            y = randint(0,9)
                            if grid.grid[x][y] == 6 or grid.grid[x][y] == 5:
                                continue
                            elif grid.grid[x][y] == 3:
                                grid.grid[x][y] = 5
                                continue
                            else:
                                grid.grid[x][y] = 6
                            if grid.check_over():
                                print("Sorry the bot beat you!!!")
                                pygame.quit()
                            break
            for key in toggles:
                if toggles[key].is_clicked(pos):
                    break
        elif toggles['voice'].activated:
            match_row = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            match_col = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet']
            col_to_num = {
                'alpha': 0,
                'bravo': 1,
                'charlie': 2,
                'delta': 3,
                'echo': 4,
                'foxtrot': 5,
                'golf': 6,
                'hotel': 7,
                'india': 8,
                'juliet': 9
            }
            while True:
                print("Speak Row (Say exit to quit)")
                y = get_speech(match_row)
                if y == 'exit':
                    done = True
                    break
                elif y != "Error":
                    y = int(y) - 1
                    break

            while True:
                print("Speak col military code (Say exit to quit)")
                print(['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet'])
                x = get_speech(match_col)
                if x == 'exit':
                    done = True
                    break
                elif x != "Error":
                    x = col_to_num[x]
                    break
            if ships:
                if toggles['vertical'].activated:
                    iteration = [0, 1]
                    orientation = 'vertical'
                else:
                    iteration = [1, 0]
                    orientation = 'horizontal'
                if ships[0].ship_to_grid((x, y), orientation, grid.grid):
                    for i in range(ships[0].size):
                        grid.grid[x][y] = 3
                        x += iteration[0]
                        y += iteration[1]
                        
                    ships.pop(0)
            # for when doing enemy ship guesses
            else:
                if enemy_grid.grid[x][y] == 6 or enemy_grid.grid[x][y] == 5:
                    pass
                elif enemy_grid.grid[x][y] == 4:
                    enemy_grid.grid[x][y] = 5
                else:
                    enemy_grid.grid[x][y] = 6
                    if enemy_grid.check_over():
                        print("You Won!!!!!")
                        pygame.quit()
                    while True:
                        x = randint(0,9)
                        y = randint(0,9)
                        if grid.grid[x][y] == 6 or grid.grid[x][y] == 5:
                            continue
                        elif grid.grid[x][y] == 3:
                            grid.grid[x][y] = 5
                            continue
                        else:
                            grid.grid[x][y] = 6
                        if grid.check_over():
                            print("Sorry the bot beat you!!!")
                            pygame.quit()
                        break

            

    # Set the screen background
    screen.fill(BLACK)


    # Draw the grid
    


    if ships:
        grid.draw(screen, font)
        text = font.render(f'Pick a head for a {ships[0].size} unit ship', True, (255,255,255), (0,0,0))
        screen.blit(text, (0, 275))
    else:
        enemy_grid.draw(screen, font)
        grid.draw(screen, font, y_displacement=300)
    # Draw the toggles
    for key in toggles:
        toggles[key].draw(screen, font)
        
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
