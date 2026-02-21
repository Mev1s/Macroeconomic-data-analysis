from csv_reader import csv_reader
from typing import Dict, List

def average_gdp_function(data: List[Dict[str, str]]) -> Dict[str, list[str]]:
    countries_gdp = {}

    for row in data: # создаем словарь с парами страна - list(ВВП)
        if row['country'] not in countries_gdp:
            countries_gdp[row['country']] = [row['gdp']]
        else:
            countries_gdp[row['country']].append(row['gdp'])
    return countries_gdp


REPORTS = {"average-gdp": average_gdp_function} # введеный аргумент (--report) = нужная функция