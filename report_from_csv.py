import numpy as np
import pandas as pd
from os import getcwd
from ydata_profiling import ProfileReport

# Path to the CSV file
data_path = getcwd() + "\data\csv_files\International_Education_Costs.csv"

# Read the CSV as a DataFrame
df = pd.read_csv(filepath_or_buffer=data_path)

# Quick inspection
df.info()

# # Convert the Visa Fee USD to 32-bit integer
# df['Visa_Fee_USD'] = df['Visa_Fee_USD'].astype(dtype=np.int32)

# # Info again
# df.info()

# # # Get everything that's a number
# # numerical_df = df.select_dtypes(include='number')

# # numerical_df.info()

# Transform the DataFrame into a Profile Report
report = ProfileReport(df=df, explorative=True, title='International Education Analytics')

# Profile Path
profile_path = getcwd() + "\data\profile_reports"

# Name of the file
file_name = 'international_education_report.html'

# Export the report to a HTML file
report.to_file(output_file=f'{profile_path}/{file_name}')