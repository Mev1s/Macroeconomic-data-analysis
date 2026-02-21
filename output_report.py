from tabulate import tabulate

def format_report(data):
    headers = ["№", "Country", "GDP"]
    return tabulate(
        data, headers=headers,
        tablefmt='psql',
        showindex=range(1, len(data) + 1),
        floatfmt=".2f"
    )