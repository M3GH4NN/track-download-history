from statistics import calculate_average_downloads, print_statistics, calculate_statistics
from models import Contributor, Resource
import pytest


def test_calculate_statistics_empty():
    with pytest.raises(ValueError) as excinfo:
        calculate_statistics({})
    assert "No contributors data to process" in str(excinfo.value)

def test_print_statistics(capsys):  # capsys is a pytest fixture that captures print statements
    contributors_stats = {'Alice': (5, 0.014)}
    print_statistics(contributors_stats)
    captured = capsys.readouterr()
    assert "Alice: 5 downloads, 0.014 downloads/day" in captured.out
