import os
import pandas as pd


def compute_distribution_stats(series: pd.Series) -> dict:
    mean_value = float(series.mean())
    median_value = float(series.median())
    min_value = float(series.min())
    max_value = float(series.max())
    std_dev_value = float(series.std())
    range_value = float(max_value - min_value)
    cv_value = float(std_dev_value / mean_value) if mean_value != 0 else 0.0

    return {
        "count": int(series.count()),
        "mean": mean_value,
        "median": median_value,
        "min": min_value,
        "max": max_value,
        "range": range_value,
        "std_dev": std_dev_value,
        "coefficient_of_variation": cv_value,
    }


def interpretation_line(column_name: str, stats: dict) -> str:
    messages = []

    if abs(stats["mean"] - stats["median"]) > 0.15 * max(stats["median"], 1.0):
        messages.append("mean and median differ notably, suggesting skew or outliers")
    else:
        messages.append("mean and median are close, suggesting a relatively stable center")

    if stats["coefficient_of_variation"] > 0.5:
        messages.append("distribution shows high relative variability")
    elif stats["coefficient_of_variation"] > 0.2:
        messages.append("distribution shows moderate variability")
    else:
        messages.append("distribution shows low relative variability")

    return f"{column_name}: " + "; ".join(messages)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "distribution_comparison_sample.csv")
    output_stats_path = os.path.join(project_root, "data", "processed", "distribution_comparison_stats.csv")
    report_path = os.path.join(project_root, "outputs", "distribution_comparison_report.txt")

    df = pd.read_csv(input_path)
    numeric_columns = ["delivery_time_min", "daily_orders", "customer_rating", "refund_amount"]

    print("Input data preview:")
    print(df.head().to_string(index=False))

    rows = []
    stats_by_column = {}

    for column in numeric_columns:
        stats = compute_distribution_stats(df[column])
        stats_by_column[column] = stats
        rows.append({"column": column, **stats})

    stats_df = pd.DataFrame(rows)
    stats_df.to_csv(output_stats_path, index=False)

    highest_mean_column = stats_df.sort_values("mean", ascending=False).iloc[0]["column"]
    highest_variability_column = stats_df.sort_values("std_dev", ascending=False).iloc[0]["column"]
    widest_range_column = stats_df.sort_values("range", ascending=False).iloc[0]["column"]

    print("\nDistribution comparison summary:")
    print(stats_df.to_string(index=False))

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Distribution Comparison Report\n")
        report.write("==============================\n")
        report.write(f"Input file: {input_path}\n\n")
        report.write("Per-column distribution statistics:\n")

        for column in numeric_columns:
            stats = stats_by_column[column]
            report.write(
                f"- {column}: mean={stats['mean']:.2f}, median={stats['median']:.2f}, "
                f"min={stats['min']:.2f}, max={stats['max']:.2f}, range={stats['range']:.2f}, "
                f"std_dev={stats['std_dev']:.2f}, cv={stats['coefficient_of_variation']:.2f}\n"
            )

        report.write("\nInterpretation notes:\n")
        for column in numeric_columns:
            report.write("- " + interpretation_line(column, stats_by_column[column]) + "\n")

        report.write("\nCross-column observations:\n")
        report.write(f"- Highest mean: {highest_mean_column}\n")
        report.write(f"- Highest spread by std_dev: {highest_variability_column}\n")
        report.write(f"- Widest value range: {widest_range_column}\n")
        report.write(
            "- These comparisons provide a baseline for asking better EDA questions before deeper analysis.\n"
        )

    print(f"\nStats table saved to: {output_stats_path}")
    print(f"Comparison report saved to: {report_path}")


if __name__ == "__main__":
    main()
