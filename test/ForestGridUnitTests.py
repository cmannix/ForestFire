import unittest
from src.ForestService import ForestService
from src.ForestGrid import ForestGrid
from src.CellState import CellState

class ForestServiceUnitTests(unittest.TestCase):
    def return_true(self): return True

    def return_false(self): return False

    def test_get_updated_state_returns_tree_state_if_empty_and_should_update(self):
        service = ForestService(0, 0)
        service.should_grow_tree = self.return_true
        has_called_should_start_fire = False
        def mock_should_start_fire(): has_called_should_start_fire = True
        service.should_start_fire = mock_should_start_fire

        grid = ForestGrid(1, service)

        new_state = grid.get_updated_state(CellState.EMPTY)

        self.assertFalse(has_called_should_start_fire)
        self.assertEquals(new_state, CellState.TREE)

    def test_get_updated_state_returns_empty_state_if_empty_and_should_not_grow(self):
        service = ForestService(0, 0)
        service.should_grow_tree = self.return_false

        has_called_should_start_fire = False
        def mock_should_start_fire(): has_called_should_start_fire = True
        service.should_start_fire = mock_should_start_fire

        grid = ForestGrid(1, service)

        new_state = grid.get_updated_state(CellState.EMPTY)

        self.assertFalse(has_called_should_start_fire)
        self.assertEquals(new_state, CellState.EMPTY)

    def test_get_updated_state_returns_fire_state_if_tree_and_should_start_fire(self):
        service = ForestService(0, 0)
        service.should_start_fire = self.return_true

        has_called_should_grow_tree = False

        def mock_should_grow_tree(): has_called_should_grow_tree = True

        service.should_grow_tree = mock_should_grow_tree

        grid = ForestGrid(1, service)

        new_state = grid.get_updated_state(CellState.TREE)

        self.assertFalse(has_called_should_grow_tree)
        self.assertEquals(new_state, CellState.FIRE)

    def test_get_updated_state_returns_tree_state_if_tree_and_should_not_start_fire(self):
        service = ForestService(0, 0)
        service.should_start_fire = self.return_false

        has_called_should_grow_tree = False

        def mock_should_grow_tree(): has_called_should_grow_tree = True

        service.should_grow_tree = mock_should_grow_tree

        grid = ForestGrid(1, service)

        new_state = grid.get_updated_state(CellState.TREE)

        self.assertFalse(has_called_should_grow_tree)

        self.assertEquals(new_state, CellState.TREE)

    def test_get_updated_state_returns_fire_state_if_fire(self):
        service = ForestService(0, 0)
        service.should_start_fire = self.return_false

        has_called_should_grow_tree = False
        has_called_should_start_fire = False

        def mock_should_start_fire(): has_called_should_start_fire = True
        def mock_should_grow_tree(): has_called_should_grow_tree = True

        service.should_start_fire = mock_should_start_fire
        service.should_grow_tree = mock_should_grow_tree

        grid = ForestGrid(1, service)

        new_state = grid.get_updated_state(CellState.FIRE)

        self.assertFalse(has_called_should_start_fire)

        self.assertFalse(has_called_should_grow_tree)

        self.assertEquals(new_state, CellState.FIRE)

    def test_spread_fire_changes_state_of_neighbour_cells(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.TREE],
                        [CellState.TREE, CellState.FIRE, CellState.TREE],
                        [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.TREE, CellState.FIRE, CellState.TREE],
                        [CellState.FIRE, CellState.EMPTY, CellState.FIRE],
                        [CellState.TREE, CellState.FIRE, CellState.TREE]]

        service = ForestService(0, 0)
        forest = ForestGrid(3, service)

        forest.grid = original_grid

        new_grid = forest.spread_fire()

        self.assertEquals(new_grid, expected_grid)

    def test_spread_fire_updates_neighbour_cells_at_border(self):
        original_grid = [[CellState.TREE, CellState.TREE, CellState.TREE],
                        [CellState.FIRE, CellState.TREE, CellState.TREE],
                        [CellState.TREE, CellState.TREE, CellState.TREE]]
        expected_grid = [[CellState.FIRE, CellState.TREE, CellState.TREE],
                        [CellState.EMPTY, CellState.FIRE, CellState.TREE],
                        [CellState.FIRE, CellState.TREE, CellState.TREE]]


        service = ForestService(0, 0)
        forest = ForestGrid(3, service)

        forest.grid = original_grid

        new_grid = forest.spread_fire()

        self.assertEquals(new_grid, expected_grid)


if __name__ == '__main__':
    unittest.main()