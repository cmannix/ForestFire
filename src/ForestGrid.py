import random
from src.CellState import CellState

class ForestGrid:
    def __init__(self, grid_size: int, growth_probability: float, fire_probability: float,
                 get_random_number=random.random):
        self.__get_random_number = get_random_number
        self._grid = self.__generate_initial_grid(grid_size, 0.55)
        self.__growth_probability = growth_probability
        self.__fire_probability = fire_probability

    def process_cells(self):
        current_grid = self._grid

        # Assume square grid
        grid_size = len(current_grid)

        new_grid = [row[:] for row in current_grid]

        def neighbour_burning(x, y):
            for dx in [-1, 1]:
                nx = x + dx
                if nx >= 0 and nx < grid_size:
                    yield current_grid[nx][y] == CellState.FIRE
            for dy in [-1, 1]:
                ny = y + dy
                if ny >= 0 and ny < grid_size:
                    yield current_grid[x][ny] == CellState.FIRE

        def should_grow_tree() -> bool:
            return self.__should_do(self.__growth_probability)

        def should_start_fire(x: int, y: int) -> bool:
            has_burning_neighbours = any(neighbour_burning(x, y))
            start_random_fire = self.__should_do(self.__fire_probability)
            return has_burning_neighbours or start_random_fire

        for x in range(grid_size):
            for y in range(grid_size):
                if (current_grid[x][y] == CellState.EMPTY and should_grow_tree()):
                    new_grid[x][y] = CellState.TREE
                elif (current_grid[x][y] == CellState.TREE and should_start_fire(x, y)):
                    new_grid[x][y] = CellState.FIRE
                elif (current_grid[x][y] == CellState.FIRE):
                    new_grid[x][y] = CellState.EMPTY

        self._grid = new_grid

    def print(self):
        for row in self._grid:
            print(row)

    @property
    def values(self):
        return [[cell_state.value for cell_state in row] for row in self._grid]

    def __should_do(self, threshold: float):
        return self.__get_random_number() <= threshold

    def __generate_initial_grid(self, grid_size: int, initial_tree_probability: float):
        def cell_state():
            is_tree = self.__should_do(initial_tree_probability)
            if is_tree:
                return CellState.TREE
            else:
                return CellState.EMPTY

        return [[cell_state() for x in range(grid_size)] for y in range(grid_size)]
