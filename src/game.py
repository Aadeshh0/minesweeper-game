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
        self._set_cell_mines_and_adjacent_counts()

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
        mine_positions = self._generate_mine_positions(coordinate_positions)
        self._place_mines(mine_positions)
        non_mine_positions = self._identify_non_mine_positions(coordinate_positions, mine_positions)
        self._set_adjacent_mine_count(non_mine_positions)

    def _generate_grid_coordinate_positions(self):
        return [(row, col) for row in range(self.height) for col in range(self.width)]
    
    def _generate_mine_positions(self, coordinate_positions) -> List[Tuple[int, int]]:
        return random.sample(coordinate_positions, self.mine_count)
    
    def _identify_non_mine_positions(self, coordinate_positions, mine_positions):
        return set(coordinate_positions) - set(mine_positions)
    
    def _place_mines(self, mine_positions):
        for row_index, column_index in mine_positions:
            self.cells[row_index][column_index].has_mine = True
        return self.cells
    
    def _is_valid_position(self, row_index:int, column_index:int) -> bool:
        return 0 <= row_index < self.height and 0 <= column_index < self.width
    
    def _set_adjacent_mine_count(self, non_mine_postitions):
        for empty_row_index, empty_column_index in non_mine_postitions:
            count = 0
            for row_index in range(empty_row_index-1, empty_row_index+2):
                for column_index in range(empty_column_index-1, empty_column_index+2):
                    if self._is_valid_position(row_index, column_index) and self.cells[row_index][column_index].has_mine:
                        count += 1
            self.cells[empty_row_index][empty_column_index].adjacent_mine_count = count

    def print(self):
        for row in self.cells:
            visible_row = [str(cell) for cell in row]
            # print(' '.join(visible_row))
            print(visible_row)

    def _is_cell_opened(self, row_index:int, column_index:int) -> bool:
        return self.cells[row_index][column_index].is_open
    
    def has_mine_at(self, coordinate:Coordinate) -> bool:
        return self.cells[coordinate.row][coordinate.column].has_mine
    
class Minesweeper:
    def __init__(self, width, height):
        self.grid = Grid(width, height)

    def _get_valid_coordinate(self, plane:str, max_index:int) -> int:
        prompt = f'Enter zero-index {plane}-coordinate between 0 and {max_index}: '

        while True:
            try:
                coordinate = int(input(prompt))
            except ValueError:
                print('Invalid input. Please enter a valid value.')
            else:
                if 0 <= coordinate <= max_index:
                    return coordinate
                else:
                    print(f'Invalid input. Please enter a number between 0 and {max_index}')

    def _get_user_guess(self) -> Coordinate:
        while True:
            print("Try to guess a non-mine. I'll ask your x and y coordinates. 0, 0  at my top left. \n Positives to right and down.")

            max_row_index = self.grid.height-1   # changes from width to heigh
            max_col_index = self.grid.width-1    # changed from height to widht

            column_index = self._get_valid_coordinate(plane = 'x', max_index=max_row_index)
            row_index = self._get_valid_coordinate(plane = 'y', max_index=max_col_index)

            if self.grid._is_cell_opened(row_index = row_index, column_index=column_index):
                print('Invalid input. The cell is already opened.')
            else:
                return Coordinate(row_index, column_index)
    
    def _has_guessed_mine(self, user_coordinate_guess:Coordinate) -> bool:
        if self.grid.has_mine_at(user_coordinate_guess):
            print('You guessed a mine.')
            return True
        else:
            return False
        
    def play(self):
        while self.grid.has_unopened_non_mines():
            self.grid.print()
            user_coordinate_guess = self._get_user_guess()
            if self._has_guessed_mine(user_coordinate_guess):
                print('You LOSE!')
                break
            else:
                self.grid.cells[user_coordinate_guess.row][user_coordinate_guess.column].open()
        else:
            print('Hooray! You won')