import csv

from parser import parse_args


def csv_reader(args):
    data = []
    for file in args.files:
        try:
            with open(file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"{file} не найден")
            return "file not found"
    return data