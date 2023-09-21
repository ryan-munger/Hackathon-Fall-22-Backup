import pygame


class Toggle:
    toggles: dict = {}
    def __init__(self, key, x_start, y_start, width, height, activated= False):
        self.key = key
        
        self.activated = activated
        self.width = width
        self.x_start = x_start
        self.x_end = x_start + width

        self.height = height
        self.y_start = y_start
        self.y_end = y_start + height
        Toggle.toggles[key] = self
    
    def is_clicked(self, pos) -> bool:
        x = pos[0]
        y = pos[1]

        if (not (self.x_start <= x)) or (not (self.x_end >= x)):
            return False
        elif (not (self.y_start <= y)) or (not (self.y_end >= y)):
            return False
        self.activated = not self.activated
        return True
    
    def draw(self, screen, font):
        if self.activated:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)

        # drawing the rectanlge
        rectangle = pygame.Rect(self.x_start, self.y_start, self.width, self.height)
        pygame.draw.rect(screen, color, rectangle)
        
        # drawing the text
        text = font.render(self.key, True, (255,255,255), (0,0,0))
        
        screen.blit(text, (self.x_end,self.y_start + (self.y_end-self.y_start)//2 - font.size(self.key)[1] //2))
        return
