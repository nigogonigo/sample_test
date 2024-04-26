import csv


def read_csv(file):
    with open(file) as f:
        rows = csv.reader(f)
        csv_header = next(rows)
        for row in rows:
            print(row[0])


csv_file = "./csv/list.csv"
read_csv(csv_file)