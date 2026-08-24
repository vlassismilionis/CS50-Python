import sys
import csv

def main():
    # Checking arguements
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    # List where data(dicts) are being stored
    data = []

    # Reading the first CSV
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                data.append({"first" : first, "last" : last, "house" : row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Writing on the second CSV
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in data:
            writer.writerow({"first" : line["first"], "last" : line["last"], "house" : line["house"]})


if __name__ == "__main__":
    main()