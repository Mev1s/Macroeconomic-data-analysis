from tabulate import tabulate

def print_report(data):
    headers = ["№", "Country", "GDP"]
    return tabulate(data, headers=headers, tablefmt='psql')