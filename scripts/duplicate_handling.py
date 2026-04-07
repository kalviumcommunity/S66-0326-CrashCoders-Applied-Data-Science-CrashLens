import os
import pandas as pd


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "sample_with_duplicates.csv")
    deduped_output_path = os.path.join(project_root, "data", "processed", "sample_deduplicated.csv")
    report_path = os.path.join(project_root, "outputs", "duplicate_handling_report.txt")

    print(f"Loading dataset: {input_path}")
    df = pd.read_csv(input_path)

    shape_before = df.shape
    print(f"Shape before deduplication: {shape_before}")

    # Keep=False marks every row that belongs to a duplicate group for inspection.
    duplicate_group_mask = df.duplicated(keep=False)
    duplicate_rows = df[duplicate_group_mask].copy()

    duplicate_count = int(df.duplicated().sum())
    print(f"Number of duplicate rows to remove (default keep='first'): {duplicate_count}")

    if not duplicate_rows.empty:
        print("\\nDuplicate rows identified:")
        print(duplicate_rows.sort_values(list(df.columns)).to_string(index=False))
    else:
        print("No duplicate rows identified.")

    deduped_df = df.drop_duplicates(keep="first").copy()
    shape_after = deduped_df.shape
    print(f"\\nShape after deduplication: {shape_after}")

    remaining_duplicates = int(deduped_df.duplicated().sum())
    print(f"Remaining duplicate rows after cleanup: {remaining_duplicates}")

    deduped_df.to_csv(deduped_output_path, index=False)

    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write("Duplicate Handling Report\\n")
        report_file.write("=========================\\n")
        report_file.write(f"Input file: {input_path}\\n")
        report_file.write(f"Shape before deduplication: {shape_before}\\n")
        report_file.write(f"Duplicate rows identified for removal: {duplicate_count}\\n")
        report_file.write(f"Shape after deduplication: {shape_after}\\n")
        report_file.write(f"Remaining duplicates after verification: {remaining_duplicates}\\n")
        report_file.write(f"Deduplicated output saved to: {deduped_output_path}\\n")

    print(f"Deduplicated dataset saved to: {deduped_output_path}")
    print(f"Verification report saved to: {report_path}")


if __name__ == "__main__":
    main()
