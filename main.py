from csv_reader import csv_reader
from parser import parse_args
from reports import avarage_gdp_function, REPORTS

if __name__ == '__main__':
    args = parse_args() # парсим аргументы
    report_function = REPORTS.get(args.report) # получаем тип отчета и название функции
    data = csv_reader(args.files) # парсим строки
    result_dict = report_function(data) # вызываем функцию отчета
