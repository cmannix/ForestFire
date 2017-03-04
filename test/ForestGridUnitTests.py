import unittest
from src.ForestGrid import *
from src.CellState import CellState

class ForestServiceUnitTests(unittest.TestCase):
    def test_process_cells_changes_empty_cells_to_trees_if_under_threshold(self):
        original_grid = [[CellState.EMPTY, CellState.EMPTY, CellState.TREE],
                         [CellState.EMPTY, CellState.TREE, CellState.TREE],
                         [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.TREE, CellState.TREE, CellState.TREE],
                         [CellState.TREE, CellState.TREE, CellState.TREE],
                         [CellState.TREE, CellState.TREE, CellState.TREE]]

        grid = ForestGrid(3, 1, 0)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)

    def test_process_cells_ignores_empty_cells_if_over_growth_threshold(self):
        original_grid = [[CellState.EMPTY, CellState.EMPTY, CellState.TREE],
                         [CellState.EMPTY, CellState.TREE, CellState.TREE],
                         [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.EMPTY, CellState.EMPTY, CellState.TREE],
                         [CellState.EMPTY, CellState.TREE, CellState.TREE],
                         [CellState.TREE, CellState.TREE, CellState.TREE]]

        grid = ForestGrid(3, 0, 0)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)

    def test_process_cells_changes_tree_cells_to_fires_if_under_threshold(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.EMPTY],
                         [CellState.TREE, CellState.EMPTY, CellState.EMPTY],
                         [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]]
        expected_grid = [[CellState.FIRE, CellState.FIRE, CellState.EMPTY],
                         [CellState.FIRE, CellState.EMPTY, CellState.EMPTY],
                         [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]]

        grid = ForestGrid(3, 0, 1)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)

    def test_process_cells_ignores_empty_cells_if_over_fire_threshold(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.EMPTY],
                         [CellState.TREE, CellState.EMPTY, CellState.EMPTY],
                         [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]]
        expected_grid = [[CellState.TREE, CellState.TREE, CellState.EMPTY],
                         [CellState.TREE, CellState.EMPTY, CellState.EMPTY],
                         [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]]

        grid = ForestGrid(3, 0, 0)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)

    def test_process_cells_changes_state_of_neighbour_cells(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.TREE],
                        [CellState.TREE, CellState.FIRE, CellState.TREE],
                        [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.TREE, CellState.FIRE, CellState.TREE],
                        [CellState.FIRE, CellState.EMPTY, CellState.FIRE],
                        [CellState.TREE, CellState.FIRE, CellState.TREE]]

        grid = ForestGrid(3, 0, 0)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)

    def test_process_cells_updates_neighbour_cells_at_border(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.TREE],
                        [CellState.FIRE, CellState.TREE, CellState.TREE],
                        [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.FIRE, CellState.TREE, CellState.TREE],
                        [CellState.EMPTY, CellState.FIRE, CellState.TREE],
                        [CellState.FIRE, CellState.TREE, CellState.TREE]]

        grid = ForestGrid(3, 0, 0)

        grid._grid = original_grid

        grid.process_cells()

        new_grid = grid._grid

        self.assertEquals(new_grid, expected_grid)


if __name__ == '__main__':
    unittest.main()