from typing import Dict, List, Union

def average_gdp_function(
        data: List[Dict[str, str]]
                         ) -> List[List[str, float]]:

    countries_gdp = {}
    result_out = []

    for row in data:
        if int(row['gdp']) < 0:
            raise ValueError(f"{row} ВВП не может быть отрицательным")
        elif row['country'] not in countries_gdp:  # создаем словарь с парами страна - list(ВВП)
            countries_gdp[row['country']] = [int(row['gdp'])]
        else: # если уже есть, то в list этой страны добавляем значение
            countries_gdp[row['country']].append(int(row['gdp']))

    for row in countries_gdp.items(): # приводим сырые данные в нужный вид
        result_out.append(
            [row[0], round(sum(row[1]) / len(row[1]), 2)]
        )

    result_out = sorted(result_out, key=lambda x: x[1], reverse=True)
    return result_out


REPORTS = {"average-gdp": average_gdp_function} # введеный аргумент (--report) = нужная функция