from src.ForestGridClass import ForestGrid
import matplotlib.pyplot as plt
import matplotlib.colors as col
from src.CellState import CellState

grid_size = 10
forest = ForestGrid.make_forest_grid(grid_size, 0.2, 0.02)

for i in range(10):
    forest.process_grid()

forest.print_grid()