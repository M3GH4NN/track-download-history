import unittest
from models import Contributor, Resource
from statistics import calculate_statistics
from unittest.mock import patch, call


class TestStatistics(unittest.TestCase):
    @patch("builtins.print")
    def test_calculate_statistics(self, mock_print):
        contributors = {"Carol": Contributor("Carol"), "Dave": Contributor("Dave")}
        contributors["Carol"].resources["res1"] = Resource("res1", 4)
        contributors["Dave"].resources["res2"] = Resource("res2", 3)
        contributors["Carol"].resources["res1"].downloads = ["2020-01-01", "2020-01-02"]
        contributors["Dave"].resources["res2"].downloads = ["2020-01-01"]

        calculate_statistics(contributors)

        # Check all calls to print and validate against expected results
        expected_calls = [
            call("Carol: 2 downloads, 0.005 downloads/day"),
            call("Dave: 1 downloads, 0.003 downloads/day"),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)


if __name__ == "__main__":
    unittest.main()
