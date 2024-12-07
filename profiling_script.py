# Import necessary libraries
import pandas as pd
from ydata_profiling import ProfileReport
from google.colab import files

# Load your dataset (replace with your dataset file path)
file_path = '/content/Store_Management_System.xlsm'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Generate the profiling report
profile = ProfileReport(df, title="Dataset Profiling Report", explorative=True)

# Save the report to an HTML file
output_file = "/content/dataset_profile_report.html"
profile.to_file(output_file)

# Download the file directly to your device
print(f"Profiling report saved as: {output_file}")
files.download(output_file)  # Triggers the download in Colab
