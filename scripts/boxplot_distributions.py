import os
import pandas as pd
import matplotlib.pyplot as plt


def compute_boxplot_stats(series: pd.Series) -> dict:
    q1 = float(series.quantile(0.25))
    median = float(series.quantile(0.50))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outlier_count = int(((series < lower_bound) | (series > upper_bound)).sum())

    return {
        "q1": q1,
        "median": median,
        "q3": q3,
        "iqr": iqr,
        "min": float(series.min()),
        "max": float(series.max()),
        "lower_bound": float(lower_bound),
        "upper_bound": float(upper_bound),
        "outlier_count": outlier_count,
    }


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    input_path = os.path.join(project_root, "data", "raw", "distribution_comparison_sample.csv")
    boxplot_image_path = os.path.join(project_root, "outputs", "boxplot_overview.png")
    report_path = os.path.join(project_root, "outputs", "boxplot_interpretation_report.txt")

    df = pd.read_csv(input_path)
    numeric_columns = ["delivery_time_min", "daily_orders", "customer_rating", "refund_amount"]

    print("Loaded dataset for boxplot visualization.")
    print("Numeric columns selected:", numeric_columns)

    plt.figure(figsize=(12, 6))
    df[numeric_columns].boxplot(grid=True)
    plt.title("Boxplot Comparison of Numeric Columns")
    plt.ylabel("Value")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(boxplot_image_path)
    plt.close()

    stats_by_column = {}
    for column in numeric_columns:
        stats_by_column[column] = compute_boxplot_stats(df[column].dropna())

    widest_iqr_column = max(stats_by_column, key=lambda col: stats_by_column[col]["iqr"])
    most_outliers_column = max(stats_by_column, key=lambda col: stats_by_column[col]["outlier_count"])

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Boxplot Interpretation Report\n")
        report.write("===========================\n")
        report.write(f"Input file: {input_path}\n")
        report.write(f"Boxplot image: {boxplot_image_path}\n\n")

        report.write("Column-wise quartile and outlier summary:\n")
        for column in numeric_columns:
            stats = stats_by_column[column]
            report.write(
                f"- {column}: min={stats['min']:.2f}, q1={stats['q1']:.2f}, median={stats['median']:.2f}, "
                f"q3={stats['q3']:.2f}, max={stats['max']:.2f}, iqr={stats['iqr']:.2f}, "
                f"outliers={stats['outlier_count']}\n"
            )

        report.write("\nCross-column observations:\n")
        report.write(f"- Widest middle spread by IQR: {widest_iqr_column}\n")
        report.write(f"- Most potential outliers by 1.5*IQR rule: {most_outliers_column}\n")
        report.write(
            "- Outliers are signals for investigation, not automatic errors to remove.\n"
        )

    print(f"Boxplot image saved to: {boxplot_image_path}")
    print(f"Interpretation report saved to: {report_path}")


if __name__ == "__main__":
    main()
