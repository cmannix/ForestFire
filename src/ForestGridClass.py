from src.ForestService import ForestService
from src.CellState import CellState

class ForestGrid:

    def __init__(self, grid_size: int, forest_service: ForestService):
        self.grid_size = grid_size
        self.service = forest_service
        self.initialise_grid()

    @classmethod
    def make_forest_grid(cls, grid_size:int, growth_probability: float, fire_probability: float):
        service = ForestService(growth_probability, fire_probability)
        return ForestGrid(grid_size, service)

    def initialise_grid(self):
        self.grid = [[CellState.EMPTY for x in range(self.grid_size)] for y in range(self.grid_size)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def process_grid(self):
        new_grid = self.spread_fire()

        self.grid[:] = [[self.get_updated_state(cell_state) for cell_state in row] for row in new_grid]

    def spread_fire(self):
        new_grid = [row[:] for row in self.grid]

        def try_burn(x, y):
            if x < 0 or y < 0 or x >= self.grid_size or y >= self.grid_size: return

            if new_grid[x][y] == CellState.TREE: new_grid[x][y] = CellState.FIRE

        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if (self.grid[x][y] == CellState.FIRE):
                    try_burn(x + 1, y)
                    try_burn(x - 1, y)
                    try_burn(x, y + 1)
                    try_burn(x, y - 1)
                    new_grid[x][y] = CellState.EMPTY

        return new_grid

    def get_updated_state(self, current_state: CellState) -> CellState:
        if (current_state == CellState.EMPTY):
            if self.service.should_grow_tree():
                return CellState.TREE

        if (current_state == CellState.TREE):
            if self.service.should_start_fire():
                return CellState.FIRE

        return current_state