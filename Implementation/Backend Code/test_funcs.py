import csv

def dict_to_csv(data, file_path):
    """
    Writes a list of dictionaries to a CSV file.

    :param data: List of dictionaries (each dictionary represents a row).
    :param file_path: Path to the output CSV file.
    """
    if not data:
        print("No data to write.")
        return

    # Extract the fieldnames (column headers) from the first dictionary
    fieldnames = data[0].keys()

    # Write the data to the CSV file
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(data)  # Write the data rows

    print(f"Data successfully written to {file_path}")