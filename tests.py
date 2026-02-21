import sys
from argparse import ArgumentParser

import pytest

from output_report import format_report
from reports import average_gdp_function as average_gdp
from parser import parse_args

dataset1 = [
    {'country': 'USA', 'gdp': '100'},
    {'country': 'USA', 'gdp': '200'},
    {'country': 'Canada', 'gdp': '150'},
    {'country': 'Mexico', 'gdp': '300'},
    {'country': 'Mexico', 'gdp': '100'},
]

dataset2 = [
    {'country': 'USA', 'gdp': '100'},
    {'country': 'USA', 'gdp': '200'},
    {'country': 'USA', 'gdp': '300'},
    {'country': 'USA', 'gdp': '400'},
    {'country': 'USA', 'gdp': '500'},
]

dataset3 = [
    {'country': 'USA', 'gdp': '100'},
    {'country': 'Canada', 'gdp': '200'},
    {'country': 'Mexico', 'gdp': '300'},
    {'country': 'Brazil', 'gdp': '400'},
    {'country': 'Chile', 'gdp': '500'},
]

dataset4 = [
    {'country': 'USA', 'gdp': '0'},
    {'country': 'USA', 'gdp': '100'},
    {'country': 'Canada', 'gdp': '0'},
    {'country': 'Mexico', 'gdp': '0'},
    {'country': 'Mexico', 'gdp': '200'},
]

dataset5 = [
    {'country': 'USA', 'gdp': '-50'},
    {'country': 'USA', 'gdp': '100'},
    {'country': 'Canada', 'gdp': '-10'},
    {'country': 'Canada', 'gdp': '50'},
    {'country': 'Mexico', 'gdp': '75'},
]


@pytest.mark.parametrize("data, expected", [
    (dataset1, 3),
    (dataset2, 1),
    (dataset3, 5),
    (dataset4, 3)
])
def test_len_result_average_gdp(data, expected): # проверяем длину массивов
    result = average_gdp(data)
    assert len(result) == expected

@pytest.mark.parametrize("data", [dataset5]) # проверка обработки отрицательного ВВП
def test_negative_value_result_average_gdp(data):
    with pytest.raises(ValueError):
        average_gdp(data)

@pytest.mark.parametrize("data, expected", [
        (
            dataset1, [
                ["Mexico", 200.0],
                ["USA", 150.0],
                ["Canada", 150.0]
        ]),
            (dataset2, [
            ["USA", 300.0]
         ])
])
def test_correctly_values_average_gdp(data, expected):
    assert average_gdp(data) == expected

def test_parser():
    sys.argv = [
        "main.py",
        "--files",
        "file.csv",
        "--report",
        "average-gdp"
    ]

    args = parse_args()

    assert args.files == ["file.csv"]
    assert args.report == "average-gdp"

def test_output_report():
    result = format_report([[1, "Mexico", 150.0]])
    assert "Mexico" in result
