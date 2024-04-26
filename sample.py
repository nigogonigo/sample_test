import csv


def compare_csv(file):
    with open(file) as f:
        rows = csv.reader(f)
        csv_header = next(rows)
        for row in rows:
            print(row[0])


list_file = "./csv/list.csv"
compare_csv(list_file)