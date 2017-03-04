import unittest
from src.ForestService import ForestService

class ForestServiceUnitTests(unittest.TestCase):

    def test_should_grow_tree_returns_true_if_random_value_less_or_equal_to_grow_probability(self):
        grow_prob = 0.2
        random_value = 0.3
        service = ForestService(grow_prob, 0)

        def mock_random(): return random_value
        service.get_random_value = mock_random

        self.assertTrue(service.should_grow_tree())

    def test_should_grow_tree_returns_false_if_random_value_greater_than_grow_probability(self):
        grow_prob = 0.2
        random_value = 0.3
        service = ForestService(grow_prob, 0)

        def mock_random(): return random_value
        service.get_random_value = mock_random

        self.assertFalse(service.should_grow_tree())

    def test_should_start_fire_returns_true_if_random_value_less_or_equal_to_fire_probability(self):
        fire_prob = 0.2
        random_value = fire_prob
        service = ForestService(0, fire_prob)

        def mock_random(): return random_value
        service.get_random_value = mock_random

        self.assertTrue(service.should_start_fire())

    def test_should_start_fire_returns_false_if_random_value_greater_than_fire_probability(self):
        fire_prob = 0.2
        random_value = 0.3
        service = ForestService(0, fire_prob)

        def mock_random(): return random_value
        service.get_random_value = mock_random

        self.assertFalse(service.should_start_fire())


if __name__ == '__main__':
    unittest.main()