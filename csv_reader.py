import csv
from typing import List, Dict
import argparse

from parser import parse_args


def csv_reader(files: argparse.Namespace) -> List[Dict[str, str]]:
    data = []
    for file in files:
        try:
            with open(file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            raise FileNotFoundError(f"{file} не найден")
    return data