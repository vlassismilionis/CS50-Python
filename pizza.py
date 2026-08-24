import sys
import csv
from tabulate import tabulate

def main():
    # Checking arguements
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # List where data(dicts) will be stored
    data = []

    try:
        type = sys.argv[1]
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({f"{type.capitalize().replace(".csv", " ")}Pizza" : row[f"{type.capitalize().replace(".csv", " ")}Pizza"], "Small" : row["Small"], "Large" : row["Large"]})
    # If file doesn't exists then exit
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Printing table with specific format
    print(tabulate(data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()