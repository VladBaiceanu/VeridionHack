import pandas as pd

# Ensure that pyarrow is installed: pip install pyarrow

def read_parquet_file(file_path, csv_output_path):
    try:
        df = pd.read_parquet(file_path, engine='pyarrow')  # Using pyarrow as the engine
        df.head(200).to_csv(csv_output_path, index=False)  # Saving the first 200 rows to a csv file
        print(f"Saved the first 200 lines to {csv_output_path}")
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function with the path to your .parquet file and the path to the output .csv file
read_parquet_file('raw/company-data-services.snappy.parquet', 'csv/company-data-services.csv')


