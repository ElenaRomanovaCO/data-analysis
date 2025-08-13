import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_csv_dataset(input_file, test_size=0.2, random_state=42):
    """
    Split a CSV file into train and test sets.
    
    Args:
        input_file (str): Path to input CSV file
        test_size (float): Proportion for test set (default: 0.2 = 20%)
        random_state (int): Random seed for reproducibility
    """
    
    # Read the CSV file
    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)
    print(f"Dataset shape: {df.shape}")
    
    # Split the data
    train_df, test_df = train_test_split(
        df, 
        test_size=test_size, 
        random_state=random_state,
        shuffle=True
    )
    
    # Create output filenames with prefixes in current directory
    base_name = os.path.splitext(input_file)[0]
    extension = os.path.splitext(input_file)[1]
    train_file = f"train_{os.path.basename(base_name)}{extension}"
    test_file = f"test_{os.path.basename(base_name)}{extension}"
    
    # Save the splits
    train_df.to_csv(train_file, index=False)
    test_df.to_csv(test_file, index=False)
    
    print(f"✅ Train set: {train_df.shape} -> {train_file}")
    print(f"✅ Test set: {test_df.shape} -> {test_file}")
    
    return train_file, test_file

# Example usage
if __name__ == "__main__":
    # Replace with your CSV filename (should be in current directory)
    input_csv = "taco_sales_2024-2025.csv"  # Change this to your actual filename
    
    # Split with default 80/20 ratio
    train_file, test_file = split_csv_dataset(
        input_file=input_csv,
        test_size=0.2,  # 20% for testing
        random_state=42  # For reproducible results
    )
    
    print("Dataset split completed!")