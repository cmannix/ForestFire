from src.ForestGrid import ForestGrid

grid_size = 10
forest = ForestGrid.from_values(grid_size, 0.2, 0.02)

for i in range(10):
    forest.process_grid()

forest.print_grid()