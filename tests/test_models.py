import unittest
from models import Contributor, Resource

class TestModels(unittest.TestCase):
    def test_contributor_creation(self):
        contributor = Contributor("Alice")
        self.assertEqual(contributor.name, "Alice")
        self.assertEqual(contributor.resources, {})

    def test_resource_creation(self):
        resource = Resource("resource1", 5)
        self.assertEqual(resource.resource_id, "resource1")
        self.assertEqual(resource.rating, 5)
        self.assertEqual(resource.downloads, [])

if __name__ == "__main__":
    unittest.main()