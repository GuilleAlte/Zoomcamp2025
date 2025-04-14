import pandas as pd

def parquet_to_csv(parquet_file, csv_file):
    """
    Reads a Parquet file and saves its content to a CSV file.

    Args:
        parquet_file (str): The path to the input Parquet file.
        csv_file (str): The path to the output CSV file.
    """
    try:
        # Read the Parquet file into a pandas DataFrame
        df = pd.read_parquet(parquet_file)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, index=False)  # index=False prevents writing the DataFrame index to the CSV

        print(f"Successfully converted '{parquet_file}' to '{csv_file}'")

    except FileNotFoundError:
        print(f"Error: Parquet file '{parquet_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage:
    input_parquet_file = "/workspaces/Zoomcamp2025/week_1_setup/2_docker_sql/yellow_tripdata_2021-01.parquet"  # Replace with the actual path to your Parquet file
    output_csv_file = "/workspaces/Zoomcamp2025/week_1_setup/2_docker_sql/yellow_tripdata_2021-01.csv"      # Replace with the desired path for your CSV file

    parquet_to_csv(input_parquet_file, output_csv_file)