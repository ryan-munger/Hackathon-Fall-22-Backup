import pygame

class Ship:
    def __init__(self, size):
        self.size= size

        
    def ship_to_grid(self, head: list[int], orientation: str, grid: list[list[int]]) -> bool:
        if orientation == 'vertical':
            iteration = [0, 1]
        elif orientation == 'horizontal':
            iteration = [1, 0]
        else:
            raise 'Orientation not defined'
        # Testing to see if it will fit and not obstruct other ships
        x, y = head
        for i in range(self.size):
            try:
                if grid[x][y] == 3:
                    return False
            except (ValueError, IndexError):
                return False
            y += iteration[1]
            x += iteration[0]
    
        # reassigning the grid to have the ships
        return True
