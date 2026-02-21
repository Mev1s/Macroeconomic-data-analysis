from csv_reader import csv_reader
from parser import parse_args
from reports import average_gdp_function, REPORTS
from output_report import print_report

if __name__ == '__main__':
    args = parse_args() # парсим аргументы
    report_function = REPORTS.get(args.report) # получаем тип отчета и название функции
    data = csv_reader(args) # парсим строки csv
    result_dict = report_function(data) # вызываем функцию отчета
    print(print_report(result_dict))

