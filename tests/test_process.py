import unittest
from io import StringIO
import sys

# Assuming these are the paths according to your project structure
from models import Contributor, Resource
from process import process_commands

class TestContributorAndResource(unittest.TestCase):
    def test_contributor_initialization(self):
        """Test Contributor initialization."""
        contributor = Contributor("Alice")
        self.assertEqual(contributor.name, "Alice")
        self.assertEqual(len(contributor.resources), 0)

    def test_resource_initialization(self):
        """Test Resource initialization."""
        resource = Resource("001", 5)
        self.assertEqual(resource.resource_id, "001")
        self.assertEqual(resource.rating, 5)
        self.assertEqual(len(resource.downloads), 0)

class TestProcessCommands(unittest.TestCase):
    def test_process_commands(self):
        """Test processing of input commands."""
        test_input = """
        Contributor Alice
        Resource Alice 001 5
        Download 001 2020-01-20
        Contributor Bob
        Resource Bob 002 3
        Download 002 2020-01-25
        """
        sys.stdin = StringIO(test_input)  # Redirect stdin to use test_input
        contributors = process_commands()
        sys.stdin = sys.__stdin__  # Reset stdin

        # Check if Contributors have been created correctly
        self.assertIn("Alice", contributors)
        self.assertIn("Bob", contributors)

        # Check if Resources have been added correctly
        self.assertIn("001", contributors["Alice"].resources)
        self.assertIn("002", contributors["Bob"].resources)

        # Check if Downloads are recorded correctly
        self.assertEqual(len(contributors["Alice"].resources["001"].downloads), 1)
        self.assertEqual(len(contributors["Bob"].resources["002"].downloads), 1)

        # Verify the specific download dates
        self.assertEqual(contributors["Alice"].resources["001"].downloads[0], "2020-01-20")
        self.assertEqual(contributors["Bob"].resources["002"].downloads[0], "2020-01-25")

if __name__ == '__main__':
    unittest.main()
