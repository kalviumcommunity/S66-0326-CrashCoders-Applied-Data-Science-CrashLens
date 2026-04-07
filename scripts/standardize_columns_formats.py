import os
import re
import pandas as pd


def standardize_column_name(column_name: str) -> str:
    cleaned = column_name.strip().lower()
    cleaned = re.sub(r"[^a-z0-9]+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "messy_format_sample.csv")
    output_path = os.path.join(project_root, "data", "processed", "standardized_format_sample.csv")
    report_path = os.path.join(project_root, "outputs", "standardization_report.txt")

    df = pd.read_csv(input_path)

    print("Before standardization")
    print("Columns:", list(df.columns))
    print("Data types:")
    print(df.dtypes)
    print(df.head().to_string(index=False))

    original_columns = list(df.columns)
    df.columns = [standardize_column_name(col) for col in df.columns]
    standardized_columns = list(df.columns)

    # Standardize text fields.
    text_columns = ["customer_name", "city_town", "status"]
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.lower().str.replace(r"\\s+", " ", regex=True)

    # Standardize numeric field.
    df["total_amount"] = (
        df["total_amount"]
        .astype(str)
        .str.replace(r"[^0-9.\-]", "", regex=True)
    )
    df["total_amount"] = pd.to_numeric(df["total_amount"], errors="coerce")

    # Standardize date field to ISO date (YYYY-MM-DD) using mixed-format parsing.
    parsed_dates = pd.to_datetime(df["order_date"], format="mixed", errors="coerce")
    df["order_date"] = parsed_dates.dt.strftime("%Y-%m-%d")

    print("\nAfter standardization")
    print("Columns:", list(df.columns))
    print("Data types:")
    print(df.dtypes)
    print(df.head().to_string(index=False))

    df.to_csv(output_path, index=False)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Column and Format Standardization Report\n")
        report.write("====================================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Output file: {output_path}\n\n")
        report.write("Column mapping (before -> after):\n")
        for before, after in zip(original_columns, standardized_columns):
            report.write(f"- {before} -> {after}\n")
        report.write("\nStandardization steps applied:\n")
        report.write("- Column names converted to snake_case\n")
        report.write("- Text columns lowercased and whitespace normalized\n")
        report.write("- total_amount cleaned and converted to numeric\n")
        report.write("- order_date parsed and converted to YYYY-MM-DD\n")
        report.write("\nPost-standardization dtype summary:\n")
        report.write(df.dtypes.to_string())
        report.write("\n")

    print(f"\nStandardized dataset saved to: {output_path}")
    print(f"Standardization report saved to: {report_path}")


if __name__ == "__main__":
    main()
