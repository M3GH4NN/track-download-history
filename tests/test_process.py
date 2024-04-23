from process import process_contributor, process_resource, process_download, ProcessError
from models import Contributor, Resource

def test_process_contributor():
    contributors = {}
    process_contributor(["Contributor", "Alice"], contributors)
    assert "Alice" in contributors
    assert isinstance(contributors["Alice"], Contributor)

def test_process_contributor_existing_raises_error():
    contributors = {"Alice": Contributor("Alice")}
    import pytest
    with pytest.raises(ProcessError) as excinfo:
        process_contributor(["Contributor", "Alice"], contributors)
    assert "already registered" in str(excinfo.value)

def test_process_resource():
    contributors = {"Alice": Contributor("Alice")}
    process_resource(["Resource", "Alice", "resource1", "5"], contributors)
    assert "resource1" in contributors["Alice"].resources
    assert contributors["Alice"].resources["resource1"].rating == 5

def test_process_download_valid():
    contributors = {"Alice": Contributor("Alice")}
    contributors["Alice"].resources["resource1"] = Resource("resource1", 5)
    process_download(["Download", "resource1", "2020-01-01"], contributors)
    assert "2020-01-01" in contributors["Alice"].resources["resource1"].downloads

def test_process_download_invalid_year():
    contributors = {"Alice": Contributor("Alice")}
    contributors["Alice"].resources["resource1"] = Resource("resource1", 5)
    process_download(["Download", "resource1", "2019-01-01"], contributors)
    assert "2019-01-01" not in contributors["Alice"].resources["resource1"].downloads
