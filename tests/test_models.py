from models import Contributor, Resource


def test_contributor_creation():
    contributor = Contributor("Alice")
    assert contributor.name == "Alice"
    assert contributor.resources == {}


def test_resource_creation():
    resource = Resource("resource1", 5)
    assert resource.resource_id == "resource1"
    assert resource.rating == 5
    assert resource.downloads == []
