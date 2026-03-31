import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    raw_data_path = os.path.join(project_root, 'data', 'raw', 'sample.csv')
    processed_data_path = os.path.join(project_root, 'data', 'processed', 'cleaned_sample.csv')
    output_report_path = os.path.join(project_root, 'outputs', 'analysis_report.txt')
    output_plot_path = os.path.join(project_root, 'outputs', 'data_plot.png')
    
    # 1. Load Raw Data (Never modify directly)
    print(f"Loading raw data from: {raw_data_path}")
    raw_df = pd.read_csv(raw_data_path)
    print(f"Loaded {len(raw_df)} rows of raw data.")
    
    # 2. Process Data (Create a new dataset)
    print("Processing data (multiplying values by 2)...")
    processed_df = raw_df.copy()
    processed_df['value_doubled'] = processed_df['value'] * 2
    
    # Save processed data separately
    print(f"Saving processed data to: {processed_data_path}")
    processed_df.to_csv(processed_data_path, index=False)
    
    # 3. Create Output Artifacts
    print("Generating output artifacts...")
    
    # Generate a report
    with open(output_report_path, 'w') as f:
        f.write("Data Analysis Report\n")
        f.write("====================\n")
        f.write(f"Number of rows processed: {len(processed_df)}\n")
        f.write(f"Average original value: {processed_df['value'].mean()}\n")
        f.write(f"Average doubled value: {processed_df['value_doubled'].mean()}\n")
    print(f"Report saved to: {output_report_path}")
    
    # Generate a plot
    plt.figure(figsize=(8, 5))
    plt.plot(processed_df['id'], processed_df['value'], label='Original Value', marker='o')
    plt.plot(processed_df['id'], processed_df['value_doubled'], label='Doubled Value', marker='s')
    plt.title('Data Analysis: Original vs Doubled Values')
    plt.xlabel('ID')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_plot_path)
    print(f"Plot saved to: {output_plot_path}")
    
    print("Data organization pipeline executed successfully! Raw data remained untouched.")

if __name__ == "__main__":
    main()
