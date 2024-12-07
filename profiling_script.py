import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

# Streamlit app
st.title("Dataset Profiling App")

# File upload
uploaded_file = st.file_uploader("Upload your Excel file", type=["xls", "xlsx", "xlsm"])
if uploaded_file is not None:
    # Load the dataset
    df = pd.read_excel(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.write(df.head())
    
    # Generate profiling report
    if st.button("Generate Profile Report"):
        with st.spinner("Generating report..."):
            profile = ProfileReport(df, title="Dataset Profiling Report", explorative=True)
            profile_path = "dataset_profile_report.html"
            profile.to_file(profile_path)
        
        # Provide download link
        with open(profile_path, "rb") as file:
            btn = st.download_button(
                label="Download Profiling Report",
                data=file,
                file_name="dataset_profile_report.html",
                mime="text/html"
            )
