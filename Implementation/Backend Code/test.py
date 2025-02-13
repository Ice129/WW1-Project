import requests
import pandas as pd

# Define the URL
url = "http://localhost:8000/import"

# Load the XLSX file and convert it to a string
def xlsx_to_string(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    # Convert the DataFrame to a CSV string
    csv_string = df.to_csv(index=False)
    return csv_string

# Path to the XLSX file
xlsx_file_path = "data/Bradford Memorials.xlsx"  # Replace with your XLSX file path

# Convert the XLSX file to a string
xlsx_data = xlsx_to_string(xlsx_file_path)

# Define the payload with the CSV string
payload = {
    "file": xlsx_data
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())