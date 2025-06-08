import random
from typing import List, Tuple
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'row column')

class Cell:
    def __init__(self, has_mine:bool, adjacent_mine_count: int, is_open=False):
        self.has_mine = has_mine
        self.adjacent_mine_count = adjacent_mine_count
        self.is_open = is_open

    def open(self):
        self.is_open = True
    
    def unopened_non_mine(self):
        return self.is_open is False and self.has_mine is False
    
    def __str__(self):

        if self.is_open:
            return str(self.adjacent_mine_count) if self.adjacent_mine_count != 0 else '0'
        else:
            return ' '
        
class Grid:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self.cells = self._create_empty_cells()

        self.mine_count = (self.width * self.height) // 4
        self._set_cell_mine_and_adjacent_counts()

    def has_unopened_non_mines(self):
        for row in self.cells:
            for cell in row:
                if cell.unopened_non_mine():
                    return True
                
        return False
    
    def _create_empty_cells(self) -> List[List[Cell]]:
        return [[Cell(has_mine=False, adjacent_mine_count=0) for _ in range(self.width)] for _ in range(self.height)]
    
    def _set_cell_mines_and_adjacent_counts(self):
        coordinate_positions = self._generate_grid_coordinate_positions()
        mine_positions = self._generate_mine_positions()
        self._place_mines(mine_positions)
        non_mine_positions = self._identify_non_mine_positions(coordinate_positions, mine_positions)
        self._set_adjacent_mine_count(non_mine_positions)

    def _generate_grid_coordinate_positions(self):
        
    
