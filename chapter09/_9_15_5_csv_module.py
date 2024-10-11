import csv


# Example 1:
#   Read a CSV file into a list of tuples.
def read_csv_data(filename):
    # newline="" denotes no newline translation.
    with open(filename, newline="") as file:
        rows = csv.reader(file)
        # First line is often a header. This reads it.
        headers = next(rows)
        # Now read the rest of the data.
        for row in rows:
            # Do something with row.
            print(row)


#   Write Python data to a CSV file.
def write_csv_data(filename, headers, rows):
    with open(filename, "w", newline="") as file:
        out = csv.writer(file)
        out.writerow(headers)
        out.writerows(rows)


# Example 2:
#   Using `DictReader()`
def read_csv_data_dr(filename):
    # newline="" denotes no newline translation.
    with open(filename, newline="") as file:
        # Interpret the first line as headers and return each row as dictionary.
        rows = csv.DictReader(file)  # <--
        for row in rows:
            # Do something with row.
            print(row)


if __name__ == "__main__":
    read_csv_data("portfolio.csv")
    read_csv_data_dr("portfolio.csv")

    headers = ["latitude", "longitude"]
    rows = [[5, 6], [6, 7]]
    write_csv_data("_9_15_5_output.csv", headers, rows)
