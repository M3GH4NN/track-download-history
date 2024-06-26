from statistics import calculate_statistics, print_statistics

import pytest


def test_calculate_statistics_empty():
    with pytest.raises(ValueError) as excinfo:
        calculate_statistics({})
    assert "No contributors data to process" in str(excinfo.value)


def test_print_statistics(capsys):
    contributors_stats = {"Alice": (5, 0.014)}
    print_statistics(contributors_stats)
    captured = capsys.readouterr()
    assert "Alice: 5 downloads, 0.014 downloads/day" in captured.out
