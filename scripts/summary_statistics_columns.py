import os
import pandas as pd


def compute_column_summary(series: pd.Series) -> dict:
    return {
        "count": int(series.count()),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "min": float(series.min()),
        "max": float(series.max()),
        "variance": float(series.var()),
        "std_dev": float(series.std()),
        "range": float(series.max() - series.min()),
    }


def format_summary_line(column_name: str, stats: dict) -> str:
    return (
        f"{column_name}: count={stats['count']}, mean={stats['mean']:.2f}, "
        f"median={stats['median']:.2f}, min={stats['min']:.2f}, max={stats['max']:.2f}, "
        f"variance={stats['variance']:.2f}, std_dev={stats['std_dev']:.2f}, range={stats['range']:.2f}"
    )


def interpretation_for_column(column_name: str, stats: dict) -> str:
    interpretations = []
    mean_median_gap = abs(stats["mean"] - stats["median"])

    if mean_median_gap > (0.15 * max(stats["median"], 1.0)):
        interpretations.append(
            "mean and median differ noticeably, suggesting possible skew or outliers"
        )
    else:
        interpretations.append("mean and median are close, suggesting relatively stable values")

    if stats["std_dev"] > (0.5 * max(stats["mean"], 1.0)):
        interpretations.append("high spread compared to average value")
    else:
        interpretations.append("moderate spread around the average")

    return f"{column_name}: " + "; ".join(interpretations)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "summary_stats_sample.csv")
    summary_csv_path = os.path.join(project_root, "data", "processed", "summary_statistics_by_column.csv")
    report_path = os.path.join(project_root, "outputs", "summary_statistics_report.txt")

    df = pd.read_csv(input_path)

    numeric_columns = ["response_time_sec", "error_count", "transaction_value"]

    print("Input dataset preview:")
    print(df.head().to_string(index=False))

    summary_rows = []
    column_summaries = {}

    for column in numeric_columns:
        stats = compute_column_summary(df[column])
        column_summaries[column] = stats
        summary_rows.append({"column": column, **stats})

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(summary_csv_path, index=False)

    most_variable_column = summary_df.sort_values("std_dev", ascending=False).iloc[0]["column"]

    print("\nColumn-wise summary statistics:")
    for column in numeric_columns:
        print(format_summary_line(column, column_summaries[column]))

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Summary Statistics Report\n")
        report.write("=========================\n")
        report.write(f"Input file: {input_path}\n\n")

        report.write("Computed statistics by numeric column:\n")
        for column in numeric_columns:
            report.write(format_summary_line(column, column_summaries[column]) + "\n")

        report.write("\nInterpretation notes:\n")
        for column in numeric_columns:
            report.write("- " + interpretation_for_column(column, column_summaries[column]) + "\n")

        report.write("\nCross-column comparison:\n")
        report.write(
            f"- Highest variability by standard deviation: {most_variable_column}\n"
        )
        report.write(
            "- Use these summaries as a first quantitative snapshot before deeper analysis.\n"
        )

    print(f"\nSummary table saved to: {summary_csv_path}")
    print(f"Interpretation report saved to: {report_path}")


if __name__ == "__main__":
    main()
