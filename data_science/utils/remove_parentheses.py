import csv
import sys
import re

# C:\Users\rev19\PycharmProjects\colledge\ADK\data-science\data_science\utils\remove_parentheses.py
# ADK\data-science\data_science\utils\data\test_taco_sales_2024-2025.csv
# ADK\data-science\data_science\utils\data\train_taco_sales_2024-2025.csv

# to run: python remove_parentheses.py data\test_taco_sales_2024-2025.csv

# to run: python remove_parentheses.py data\train_taco_sales_2024-2025.csv


def remove_parentheses_from_csv(filename):
    """Remove parentheses from CSV column headers"""
    
    # Read the original file
    with open(filename, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)
    
    if not rows:
        print("CSV file is empty")
        return
    
    # Process headers (first row)
    headers = rows[0]
    new_headers = []
    
    for header in headers:
        # Remove parentheses and their contents
        new_header = re.sub(r'\([^)]*\)', '', header).strip()
        # Clean up any double spaces
        new_header = ' '.join(new_header.split())
        new_headers.append(new_header)
    
    rows[0] = new_headers
    
    # Write back to the same file
    with open(filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)
    
    print(f"Updated {filename}")
    print(f"Old headers: {headers}")
    print(f"New headers: {new_headers}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    remove_parentheses_from_csv(filename)