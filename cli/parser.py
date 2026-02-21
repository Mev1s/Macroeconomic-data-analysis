import argparse


parser = argparse.ArgumentParser(description='csv_report_generator')
parser.add_argument('--files', required=True, nargs='*', help='csv files')
parser.add_argument('--report', required=True, help='report type')
args = parser.parse_args()


files = args.files
report = args.report