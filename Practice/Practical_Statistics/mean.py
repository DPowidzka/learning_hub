import pandas as pd
from scipy.stats import trim_mean   # import function for calculating trimmed average
import numpy as np


# Read the CSV file
data_science_salary = pd.read_csv('LearningLog/Practical_Statistics/DataSets/ds_salaries.csv')

# Display first five rows for reference
print(data_science_salary.head())

# Drop missing values
salaries = data_science_salary['salary_in_usd'].dropna()

# Check the categories in experience_level
experience_summary = data_science_salary.groupby('experience_level').size()

# Define weights for experience level
experience_weights = {
    'EN': 1,
    'MI': 2,
    'SE': 3,
    'EX': 4,
}

# Map the experience levels to weights
data_science_salary['weight'] = data_science_salary['experience_level'].map(experience_weights)

# Calculate basic statistics
mean_salary = salaries.mean()
trimmed_mean_salary = trim_mean(salaries, 0.1)
median_salary = salaries.median()
std_salary = salaries.std()
mode_salary = salaries.mode()[0]  # Handle cases with multiple modes
weighted_avg_salary = np.average(salaries, weights=data_science_salary['weight'])


# Print statistics
print("\n--- Salary Statistics ---")
print(f"Mean salary: {mean_salary.round(2)} - Average of all values.")
print(f"Trimmed mean salary: {trimmed_mean_salary.round(2)} - Mean with 10% of values trimmed from each end to reduce impact of outliers.")
print(f"Median salary: {median_salary.round(2)} - The middle value, providing a robust measure of central tendency.")
print(f"Standard deviation: {std_salary.round(2)} - Shows the spread of the salaries.")
print(f"Mode salary: {mode_salary} - The most frequently occurring salary.")
print(f'Weighted average salary: {weighted_avg_salary.round(2)} - Average salary including experience level')