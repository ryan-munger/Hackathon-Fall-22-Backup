import pygame

class Grid():

    def __init__(self, size, WHITE, GREEN, MARGIN, HEIGHT, WIDTH, GREY, RED, BLUE):
        self.WHITE = WHITE
        self.GREEN = GREEN
        self.MARGIN = MARGIN
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.GREY = GREY
        self.RED = RED
        self.BLUE = BLUE

        self.x_start = 0 
        self.x_end = self.WIDTH * 10 + MARGIN * 10
        self.y_start = 0
        self.y_end = self.WIDTH * 10 + MARGIN * 10

        self.grid = []
        for row in range(size):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(size):
                self.grid[row].append(0)  # Append a cell
        
    def draw(self, screen, font, y_displacement=0) -> None:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J']
        for row in range(10):
            text = font.render(str(row+1), True, (255,255,255), (0,0,0))
            screen.blit(text, ((self.WIDTH + self.MARGIN)*10 + 5, (self.MARGIN + self.HEIGHT) * row + self.MARGIN - font.size(str(row+1))[1] //2 + 10))
            
            for column in range(10):
                color = self.WHITE
                if self.grid[column][row] == 1:
                    color = self.GREEN
                elif self.grid[column][row] == 3:
                    color = self.GREY
                elif self.grid[column][row] == 5:
                    color = self.RED
                elif self.grid[column][row] == 6:
                    color = self.BLUE
                pygame.draw.rect(screen,
                                color,
                                [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                (self.MARGIN + self.HEIGHT) * row + self.MARGIN + y_displacement,
                                self.WIDTH,
                                self.HEIGHT])

            text = font.render(letters[row], True, (255,255,255), (0,0,0))
            screen.blit(text, ((self.WIDTH + self.MARGIN+ 2) * row, (self.HEIGHT + self.MARGIN)*10 ))
            
    
    def is_clicked(self, pos: tuple[int]) -> bool:
        x = pos[0]
        y = pos[1]
        
        if (not (self.x_start <= x)) or (not (self.x_end >= x)):
            return False
        elif (not (self.y_start <= y)) or (not (self.y_end >= y)):
            return False
        return True

    def change_pos(self, pos, value) -> None:
        x, y = pos
        self.grid[x][y] = value
        return
    
    def check_over(self) -> bool:
        for row in self.grid:
            for val in row:
                if val == 4 or val == 3:
                    return False
        return True
        