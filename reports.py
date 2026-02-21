from csv_reader import csv_reader
from typing import Dict, List

def average_gdp_function(
        data: List[Dict[str, str]]
                         ) -> List[list[int, str, float]]:

    countries_gdp = {}
    result_out = []

    for row in data:
        if row['country'] not in countries_gdp:  # создаем словарь с парами страна - list(ВВП)
            countries_gdp[row['country']] = [int(row['gdp'])]
        else: # если уже есть, то в list этой страны добавляем значение
            countries_gdp[row['country']].append(int(row['gdp']))

    for ind, row in enumerate(countries_gdp.items()): # приводим сырые данные в нужный вид
        result_out.append(
            [ind+1, row[0], round(sum(row[1]) / len(row[1]), 2)]
        )

    result_out = sorted(result_out, key=lambda x: x[2], reverse=True)

    return result_out


REPORTS = {"average-gdp": average_gdp_function} # введеный аргумент (--report) = нужная функция