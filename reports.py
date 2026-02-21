from csv_reader import csv_reader

def avarage_gdp_function():
    countries_gdp = {}


    for row in data: # создаем словарь с парами страна - list(ВВП)
        if row['country'] not in countries_gdp:
            countries_gdp[row['country']] = int(row['gdp'])
        else:
            countries_gdp[row['country']].append(row['gdp'])
    print(countries_gdp)



REPORTS = {"avarage-gdp": avarage_gdp_function}