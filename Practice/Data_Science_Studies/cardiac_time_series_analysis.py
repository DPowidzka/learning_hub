import os
import pandas as pd
import numpy as np


def calculate_statistics(data: pd.DataFrame, column: str) -> dict:
    """Calculate descriptive statistics for a given column in the data.

    Args:
        data (pd.DataFrame): The DataFrame containing the data.
        column (str): The column name for which to calculate statistics.

    Returns:
        dict: A dictionary with keys 'mean', 'std', 'median', 'min', 'max', and 'count', representing respective statistics for the column.
    """
    return {
        'mean': np.mean(data[column]),
        'std': np.std(data[column]),
        'median': np.median(data[column]),
        'min': np.min(data[column]),
        'max': np.max(data[column]),
        'count': len(data[column])
    }


def process_file(filepath: str, segment_type: str, segment_value: int) -> dict:
    """Process a single .tti file and compute statistics for the selected segment.

    Args:
        filepath (str): Path to the .rri file.
        segment_type (str): Segment type ('T' for time, 'N' for number of rows).
        segment_value (int): Value specifying the time limit (in minutes) or number of rows.

    Returns:
        dict: A dictionary where keys are variable names, and values are dictionaries containing descriptive statistics for eac variable.
    """
    # Read the data from the .rri file
    data = pd.read_csv(filepath, sep="\t")

    # Select the appropriate segment based on user input
    if segment_type == 'T':
        # Filter rows where 'time[min]' is within the specified time range
        segment = data[data['time[min]'] <= segment_value]
    elif segment_type == 'N':
        # Select the first N rows of the dataset
        segment = data.iloc[:segment_value]
    else:
        raise ValueError("Invalid segment type. Use 'T' for time or 'N' for rows.")
    

    # Compute statistics for relevant columns
    stats = {}
    for column in ['rri[ms]', 'rr-flags[]', 'rr-systolic[mmHg]', 'rr-diastolic[mmHg]', 'rr-mean[mmHg]']:
        column_stats = calculate_statistics(segment, column)
        # Flatten the dictionary: each stat (e.g., mean, std) becomes a separate key
        for stat, value in column_stats.items():
            stats[f'{column}_{stat}'] = value

    return stats


def save_results(results: dict, output_file: str) -> None:
    """Save the computed statistics to a CSV file.

    Args:
        results (dict): A dictionary where keys are file names, and values are dictionaries containing statistics for variables.
        output_file (str): Path to the output CSV file.
    """
    all_stats = []

    # Prepare a list of dictionaries for each file's statistics (one row per file)
    for file, stats in results.items():
        stats['File'] = file  # Add the file name
        all_stats.append(stats)

    # Check if the file already exists, and if so, increment the filename
    if os.path.exists(output_file):
        base, ext = os.path.splitext(output_file)
        counter = 1
        # Add a number to the file name if it exists
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        output_file = f"{base}_{counter}{ext}"

    # Convert the list of dictionaries to a DataFrame and save it as a CSV
    df = pd.DataFrame(all_stats)
    # Reorder columns to ensure 'File' is the first column
    columns = ['File'] + [col for col in df.columns if col != 'File']
    df = df[columns]
    # Save the DataFrame to the CSV file
    df.to_csv(output_file, index=False)


def main(input_folder: str, output_file: str, segment_type: str, segment_value: int) -> None:
    """Main function to process all files in the input folder, compute statistics, and save results.

    Args:
        input_folder (str): Path to the folder containing .rri files.
        output_file (str): Path to the output CSV file.
        segment_type (str): Segment type ('T' for time, 'N' for number of rows).
        segment_value (int): alue specifying the time limit (in minutes) or number of rows.
    """
    results = {}

    # Process each .rri file in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".rri"): # Only process files with .rri extension
            filepath = os.path.join(input_folder, file)
            print(f"Processing {file}...")
            results[file] = process_file(filepath, segment_type, segment_value)

    # Save the aggregated results to the specified CSV file
    save_results(results, output_file)
    print(f'Results saved to {output_file}')


if __name__ == "__main__":
    # User inputs
    input_folder = r"C:\Users\domin\Desktop\Dominika\DS\DS_TypyDanych\ds"  # Folder path
    output_file = "results.csv"

    # Prompt the user for segment type and value
    segment_type = input("Enter segment type ('T' for time, 'N' for rows):").strip()
    segment_value = int(input(f"Enter segment value (time in minutes or number of rows): "))

    # Run the main analysis function
    main(input_folder, output_file, segment_type, segment_value)

